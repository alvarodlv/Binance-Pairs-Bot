from decouple import config

# SELECT MODE
MODE = 'TEST'

# Close all open positions and orders
ABORT_ALL_POSITIONS = False

# Find cointegrated pairs
FIND_CONITEGRATED = True

# Place trades
PLACE_TRADES = True

# Resolution
RESOLUTION = "1 HOUR"

# Stats window
WINDOW = 21

# Thresholds - Opening
MAX_HAF_LIFE = 24
ZSCORE_THRESH = 1,5
USD_PER_TRADE = 50
USD_MIN_COLLATERAL = 1800

# Thresholds - Closing
CLOSE_AT_ZSCORE_CROSS = True

# API keys
API_KEY = config('API_KEY')
SECRET_KEY = config('SECRET_KEY')
TEST_API_KEY = config('TEST_API_KEY')
TEST_SECRET_KEY = config('TEST_SECRET_KEY')
KEY = API_KEY if MODE != 'TEST' else TEST_API_KEY
SECRET = SECRET_KEY if MODE != 'TEST' else TEST_SECRET_KEY