import numpy as np
import cryptocompare as cc
import yfinance as yfin
import matplotlib
import datetime as dt

d1= dt.datetime(2021,1,1)
d2= dt.datetime(2021,1,15)
d3= dt.datetime(2021,2,1)
d4= dt.datetime(2021,2,15)
d5= dt.datetime(2021,3,1)
d6= dt.datetime(2021,3,15)

date_arr = np.array([d1,d2,d3,d4,d5,d6])
crypto_arr = np.array(['LINK','ETH','XRP','ADA'])
eth = np.array([ETH])
link

price = cc.get_historical_price(crypto_arr[0],'USD',date_arr[0],'Kraken')
print(price['LINK']['USD'])
price_2 = cc.get_historical_price('ETH','USD',dt.datetime(2021,1,1),'Kraken')
print(price_2['ETH']['USD'])
price_3 = cc.get_historical_price('XRP','USD',dt.datetime(2021,1,1),'Kraken')
print(price_3['XRP']['USD'])
price_4 = cc.get_historical_price('ADA', 'USD',dt.datetime(2021,1,1),'Kraken')
print(price_4['ADA']['USD'])

link_arr = np.array([])
