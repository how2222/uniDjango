from django.shortcuts import render, redirect
import yfinance as yf
import datetime
import json

def index(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        period = request.POST.get('period', '30')
        period_unit = request.POST.get('period_unit', 'days')
        
        if symbol:
            return redirect(f'/graph/?symbol={symbol}&period={period}&period_unit={period_unit}')
        else:
            return render(request, 'home/index.html', {'error': 'Veuillez entrer un symbole.'})

    return render(request, 'home/index.html')
def graph(request):
    symbol = request.GET.get('symbol')
    period = request.GET.get('period', '30')
    period_unit = request.GET.get('period_unit', 'days')
    
    print(f"Symbol reçu: {symbol}, Période: {period} {period_unit}")
    error = None
    
    if symbol:
        try:
            period_value = int(period)
            
            end_date = datetime.datetime.now()
            
            if period_unit == 'hours':
                start_date = end_date - datetime.timedelta(hours=period_value)
                interval = '1h'
                print(f"Mode horaire: intervalle = {interval}")
            else:
                start_date = end_date - datetime.timedelta(days=period_value)
                interval = '1d' 
                
            print("Recherche de données pour", symbol, "du", start_date, "au", end_date)
            
            
            data = yf.download(symbol, start=start_date, end=end_date, interval=interval)
            ticker = yf.Ticker(symbol)
            currency = ticker.info.get('currency', 'N/A')
            timezone = ticker.info.get('exchangeTimezoneName', 'N/A')
            company_name = ticker.info.get('longName', symbol)


            print("Données vides?", data.empty)
            
            if not data.empty and 'Close' in data.columns:
                date_format = '%Y-%m-%d %H:%M' if period_unit == 'hours' else '%Y-%m-%d'
                
                chart_data = {
                    'dates': data.index.strftime(date_format).tolist(),
                    'prices': [prices[0] for prices in data['Close'].values.tolist()]
                }
                print("Données de graphique:", chart_data)
                context = {
                    'chart_data': json.dumps(chart_data),
                    'symbol': symbol,
                    'period': period,
                    'period_unit': period_unit,
                    'currency': currency,
                    'timezone': timezone,
                    'company_name': company_name
                }
                print("Rendu de graph.html avec symbole:", symbol)
                return render(request, 'home/graph.html', context)
            else:
                error = f"Aucune donnée trouvée pour le symbole '{symbol}'."
                print("Pas de données:", error)
        except Exception as e:
            error = f"Erreur lors de la récupération des données : {str(e)}"
            print("Exception:", error)
            
        print("Rendu de index.html avec erreur:", error)
        return render(request, 'home/index.html', {
            'error': error, 
            'symbol': symbol,
            'period': period,
            'period_unit': period_unit
        })
    else:
        print("Aucun symbole fourni, redirection vers l'accueil")
        return redirect('/')