from binanceAPICalls import BinanceAPICalls
from functions import print_json
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import coint


# Download close prices for symbols
#prices, returns = API.get_close_prices(client,symbols=['DOGEUSDT','WAVESUSDT'],interval="1h",start="2023-09-24")


# Connect to Binance
API = BinanceAPICalls(True)
client = API.api_login()

# Place market order to open/close positons
order = API.place_market_order(client, symbol='BTCBUSD', side='SELL', order_type='MARKET', quantity=0.0005)
info = API.get_order_info(client, order)

# Abort all open orders


# Construct market prices to build table


# Store cointegrated pairs 


# While TRUE:
# Manage existing trades

# Open positions