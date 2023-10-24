from binanceAPICalls import BinanceAPICalls
from functions import print_json
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import coint


# Initiate API object
API = BinanceAPICalls(False)
client = API.api_login()

# Download close prices for symbols
prices, returns = API.get_close_prices(client,symbols=['DOGEUSDT','WAVESUSDT'],interval="1h",start="2023-09-24")

plt.plot(prices.index, prices)
plt.show()