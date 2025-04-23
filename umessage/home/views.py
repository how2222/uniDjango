from django.shortcuts import render
import yfinance as yf
import datetime
import json

def index(request):
    if request.method == 'POST':
        symbol = request.POST.get('symbol')
        if symbol:
            # Récupère les données sur 1 mois
            end_date = datetime.datetime.now()
            start_date = end_date - datetime.timedelta(days=30)
            data = yf.download(symbol, start=start_date, end=end_date)

            # Préparer les données pour le graphique
            chart_data = {
                'dates': data.index.strftime('%Y-%m-%d').tolist(),
                'prices': data['Close'].fillna(0).tolist()
            }

            context = {
                'chart_data': json.dumps(chart_data),
                'symbol': symbol
            }
            return render(request, 'home/graph.html', context)
    
    return render(request, 'home/index.html')
