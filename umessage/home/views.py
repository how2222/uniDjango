from django.shortcuts import render
import pytz
import yfinance as yf
import datetime
import json

def index(request):
    context = {}
    
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        period = request.POST.get('period', '30')
        period_unit = request.POST.get('period_unit', 'days')
        
        if symbol:
            try:
                ticker = yf.Ticker(symbol)
                timezone = ticker.info.get('exchangeTimezoneName', 'N/A')
                if timezone != 'N/A':
                    exchange_tz = pytz.timezone(timezone)
                else:
                    exchange_tz = pytz.timezone('US/Eastern')

                period_value = int(period)
                
                end_date = datetime.datetime.now(exchange_tz)
                
                if period_unit == 'hours':
                    start_date = end_date - datetime.timedelta(hours=period_value)
                    interval = '1h'
                elif period_unit == 'minutes':
                    start_date = end_date - datetime.timedelta(minutes=period_value)
                    interval = '1m'
                else:
                    start_date = end_date - datetime.timedelta(days=period_value)
                    interval = '1d'            
                
                data = yf.download(symbol, start=start_date, end=end_date, interval=interval)

                currency = ticker.info.get('currency', 'N/A')
                company_name = ticker.info.get('longName', symbol)
                
                if not data.empty and 'Close' in data.columns:
                    if interval == '1m':
                        date_format = '%Y-%m-%d %H:%M:%S'
                    elif interval == '1h':
                        date_format = '%Y-%m-%d %H:%M'
                    else:
                        date_format = '%Y-%m-%d'
                    
                    chart_data = {
                        'dates': data.index.strftime(date_format).tolist(),
                        'prices': [prices[0] for prices in data['Close'].values.tolist()]
                    }
                    
                    context.update({
                        'chart_data': json.dumps(chart_data),
                        'symbol': symbol,
                        'period': period,
                        'period_unit': period_unit,
                        'currency': currency,
                        'timezone': timezone,
                        'company_name': company_name,
                        'show_graph': True
                    })
                else:
                    context['error'] = f"No data for '{symbol}'."
            except Exception as e:
                context['error'] = f"error : {str(e)}"
        else:
            context['error'] = 'Please enter an index.'
            
        context.update({
            'symbol': symbol,
            'period': period,
            'period_unit': period_unit
        })
            
    return render(request, 'home/index.html', context)