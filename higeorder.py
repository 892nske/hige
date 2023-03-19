import ccxt
import time
import pandas as pd
import json

with open('api.json') as f:
    apf = json.load(f)

bybit = ccxt.bybit({"apiKey":apf["api_key"], "secret":apf["secret_key"]})

dif = 250
dp=120
dl=120

cancel_order = bybit.cancelAllOrders(symbol = "BTCUSDT")
pos = bybit.fetchPositions()
posl = [p['data'] for p in pos]
posd=pd.DataFrame(posl)
if (posd['size']!='0').sum() == 0:
    ticker_info = bybit.fetch_ticker(symbol = 'BTCUSDT')
    order = bybit.create_order('BTCUSDT','limit','buy',0.001,ticker_info['last']-dif,{'take_profit': ticker_info['last']-dif+dp,'stop_loss': ticker_info['last']-dif-dl})
    order = bybit.create_order('BTCUSDT','limit','sell',0.001,ticker_info['last']+dif,{'take_profit': ticker_info['last']+dif-dp,'stop_loss': ticker_info['last']+dif+dl})