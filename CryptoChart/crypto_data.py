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

link_d1 = cc.get_historical_price(crypto_arr[0],'USD',date_arr[0],'Kraken')
link_d2 = cc.get_historical_price(crypto_arr[0],'USD',date_arr[1],'Kraken')
link_d3 = cc.get_historical_price(crypto_arr[0],'USD',date_arr[2],'Kraken')
link_d4= cc.get_historical_price(crypto_arr[0],'USD',date_arr[3],'Kraken')
link_d5= cc.get_historical_price(crypto_arr[0],'USD',date_arr[4],'Kraken')
link_d6 = cc.get_historical_price(crypto_arr[0],'USD',date_arr[5],'Kraken')

usd_link_d1 = link_d1.get('LINK')
usd_link_d2 = link_d2.get('LINK')
usd_link_d3 = link_d3.get('LINK')
usd_link_d4 = link_d4.get('LINK')
usd_link_d5 = link_d5.get('LINK')
usd_link_d6 = link_d6.get('LINK')


link_arr = np.array([usd_link_d1,usd_link_d2,usd_link_d3,usd_link_d4,usd_link_d5,usd_link_d6])

eth_d1 = cc.get_historical_price(crypto_arr[1],'USD',date_arr[0],'Kraken')
eth_d2 = cc.get_historical_price(crypto_arr[1],'USD',date_arr[1],'Kraken')
eth_d3 = cc.get_historical_price(crypto_arr[1],'USD',date_arr[2],'Kraken')
eth_d4= cc.get_historical_price(crypto_arr[1],'USD',date_arr[3],'Kraken')
eth_d5= cc.get_historical_price(crypto_arr[1],'USD',date_arr[4],'Kraken')
eth_d6 = cc.get_historical_price(crypto_arr[1],'USD',date_arr[5],'Kraken')

usd_eth_d1 = eth_d1.get('ETH')
usd_eth_d2 = eth_d2.get('ETH')
usd_eth_d3 = eth_d3.get('ETH')
usd_eth_d4 = eth_d4.get('ETH')
usd_eth_d5 = eth_d5.get('ETH')
usd_eth_d6 = eth_d6.get('ETH')


eth_arr = np.array([usd_eth_d1,usd_eth_d2,usd_eth_d3,usd_eth_d4,usd_eth_d5,usd_eth_d6])

xrp_d1 = cc.get_historical_price(crypto_arr[2],'USD',date_arr[0],'Kraken')
xrp_d2 = cc.get_historical_price(crypto_arr[2],'USD',date_arr[1],'Kraken')
xrp_d3 = cc.get_historical_price(crypto_arr[2],'USD',date_arr[2],'Kraken')
xrp_d4= cc.get_historical_price(crypto_arr[2],'USD',date_arr[3],'Kraken')
xrp_d5= cc.get_historical_price(crypto_arr[2],'USD',date_arr[4],'Kraken')
xrp_d6 = cc.get_historical_price(crypto_arr[2],'USD',date_arr[5],'Kraken')

usd_xrp_d1 = xrp_d1.get('XRP')
usd_xrp_d2 = xrp_d2.get('XRP')
usd_xrp_d3 = xrp_d3.get('XRP')
usd_xrp_d4 = xrp_d4.get('XRP')
usd_xrp_d5 = xrp_d5.get('XRP')
usd_xrp_d6 = xrp_d6.get('XRP')

xrp_arr = np.array([usd_xrp_d1,usd_xrp_d2,usd_xrp_d3,usd_xrp_d4,usd_xrp_d5,usd_xrp_d6])

ada_d1 = cc.get_historical_price(crypto_arr[3],'USD',date_arr[0],'Kraken')
ada_d2 = cc.get_historical_price(crypto_arr[3],'USD',date_arr[1],'Kraken')
ada_d3 = cc.get_historical_price(crypto_arr[3],'USD',date_arr[2],'Kraken')
ada_d4= cc.get_historical_price(crypto_arr[3],'USD',date_arr[3],'Kraken')
ada_d5= cc.get_historical_price(crypto_arr[3],'USD',date_arr[4],'Kraken')
ada_d6 = cc.get_historical_price(crypto_arr[3],'USD',date_arr[5],'Kraken')

usd_ada_d1 = ada_d1.get('ADA')
usd_ada_d2 = ada_d2.get('ADA')
usd_ada_d3 = ada_d3.get('ADA')
usd_ada_d4 = ada_d4.get('ADA')
usd_ada_d5 = ada_d5.get('ADA')
usd_ada_d6 = ada_d6.get('ADA')

ada_arr = np.array([usd_ada_d1,usd_ada_d2,usd_ada_d3,usd_ada_d4,usd_ada_d5,usd_ada_d6])

print(date_arr)
print(link_arr)
print(eth_arr)
print(xrp_arr)
print(ada_arr)
