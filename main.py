import matplotlib.pyplot as plt

from binanceAPICalls import BinanceAPICalls
from functions import print_json
from statsmodels.tsa.stattools import coint
from binance.enums import *
from constants import *


# Download close prices for symbols
#prices, returns = API.get_close_prices(client,symbols=['DOGEUSDT','WAVESUSDT'],interval="1h",start="2023-09-24")


# Connect to Binance
API = BinanceAPICalls(True if MODE == 'TEST' else False)
client = API.api_login()

# Place market order to open/close positons


# Abort all open orders
if ABORT_ALL_POSITIONS:
    close_orders = API.abort_all_positions(client)

# Construct market prices to build table


# Store cointegrated pairs 


# While TRUE:
# Manage existing trades

# Open positions