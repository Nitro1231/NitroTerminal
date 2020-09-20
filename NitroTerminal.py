import time
import investpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

soaringGap = 3 * 7 # 3 week

def getSoaringStock():
    currentDate = datetime.datetime.today().strftime('%d/%m/%Y')
    startDate = (datetime.datetime.today() - datetime.timedelta(soaringGap)).strftime('%d/%m/%Y')
    stocks = investpy.get_stocks(country='United States')

    i = 0
    soaringStocks = []
    for s in stocks['symbol']:
        try:
            com = investpy.get_stock_historical_data(stock=s, country='United States', from_date=startDate, to_date=currentDate)
            avgVol = 0
            currentVol = com['Volume'][len(com) - 1]

            for data in com['Volume']:
                avgVol += int(data)
                
            avgVol -= currentVol
            avgVol = avgVol / (len(com) - 1)
            isSoaringStock = (currentVol >= avgVol * 8) # 800%

            if (isSoaringStock and avgVol != 0 and currentVol != 0):
                soaringStocks.append(s)
                print(f'[Info] {s}')
                print(f'Mean: {avgVol}')
                print(f'Current: {currentVol}')
                print(f'SoaringStock: {isSoaringStock}')
            else:
                i += 1
                print(f'[{i}/{len(stocks)}] {s}')
        except:
            print(f'[{i}/{len(stocks)}] {s} - Err')

    print(soaringStocks)
        
getSoaringStock()