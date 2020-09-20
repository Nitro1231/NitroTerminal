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
            i += 1
            print(f'[{i}/{len(stocks)}] {s} - Err')

    print(soaringStocks)
        
getSoaringStock()

# ATI, HRB, TER, RGRNF, ARAY, ARTW, ATNI, PTVCB, CIZN, CLRO, EGLE, FUNC, GERN, BREW, ITRN, JAZZ, MMLP, SNOA, OPOF, GSV, BHB, CVM, CIX, FSP, GV, ISR, NTN, NHC, RLGT, RVP, SIF, TGC, TMP, BTG, VNRX, PHI, PEI, CLI, MYE, NL, BFS, SOL, ALSMY, ALNPY, BKEAY, CMPGY, CPKPY, DQJCY, GBOOY, GTMAY, JGCCY, MTNOY, PCCWY, SSLZY, WLMIY, FERGY, HENOY, KLBAY, SGTZY, SMUUY, CTLT, SFST, LMRK, FMAO, BFST, MEDP, QADB, TCX, MJCO, PT, YORW, WPRT, FOXF, WING, PLL, TC, GWGH, AHCO, ALRS, TIGO, BVN, BTG, ERA