import os
import logging
import pandas as pd
import numpy as np

from functions import initiate_logger, validate_key
from binance.client import Client
from dotenv import load_dotenv
from datetime import datetime as dt

class BinanceAPICalls:
    def __init__(self, testnet):
        logging.basicConfig(level=logging.DEBUG, filename='logs/api_log.log', format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
        self.testnet = testnet
        self.logger = initiate_logger('logs/api_log.log')

    def api_login(self):
    
        # Logger
        site = 'TestNet' if self.testnet else 'Live'
        self.logger.info(f'[START] Initiating login to {site} API')

        # Load in and validate keys
        load_dotenv()
        if self.testnet == False:
            api_key = os.environ['API_KEY']
            api_secret = os.environ['SECRET_KEY']
            validate_key(self.logger, api_key,api_secret)
            self.logger.info('[DEQUEUED] Test keys saved.')
        else:    
            api_key = os.environ['TEST_API_KEY']
            api_secret = os.environ['TEST_SECRET_KEY']
            validate_key(self.logger, api_key,api_secret)
            self.logger.info('[DEQUEUED] Live keys saved.')

        # Initiate Binance API
        try:
            client = Client(api_key, api_secret, testnet=self.testnet)
            client.get_account()
            self.logger.info(f'[COMPLETE] Connected to {site} API.')
        except Exception:
            self.logger.exception(f'[ERROR] Failed to connect to the {site} API.')
            raise

        return client    
    
    def account(self, client):
        
        self.logger.info(f'[START] Accessing account balance infromation.') 
        try:
            info = client.get_account()
            self.logger.info('[COMPLETE] Account information saved.')
        except:
            self.logger.exception('[ERROR] Unable to fetch account details.')

        return info
    
    def balance(self, client, asset):

        self.logger.info(f'[START] Accessing {asset} balance infromation.')  
        if isinstance(asset, list):
            try:
                acc_info = client.get_account()
                info = []
                for i in acc_info['balances']:
                    if i['asset'] in asset:
                        info.append(i)
                info_print = [[i['asset'],i['free']] for i in info]
                self.logger.info(f'[COMPLETE] Balance information saved: {info_print}')
            except: 
                self.logger.exception(f'[ERROR] Unable to fetch asset balances {asset}.')
        else:
            try:
                info = client.get_asset_balance(asset=asset)
                info_print = [info['asset'], info['free']]
                self.logger.info(f'[COMPLETE] Balance information saved: {info_print}')
            except:
                self.logger.exception(f'[ERROR] Unable to fetch asset balance {asset}.')

        return info
    
    def get_close_prices(self, client, symbols, interval, start=None):

        # Initialise results dataframes
        self.logger.info(f'[START] Initiating close price download for: {symbols}')
        data = pd.DataFrame()
        returns = pd.DataFrame()

        # Loop through symbols and pull/save data
        for i in symbols:
            try:
                klines = client.get_historical_klines(i, interval, start if start is not None else '')
                prices = pd.DataFrame(klines)
                prices.columns = ['open_time','open', 'high', 'low', 'close', 'volume','close_time', 'qav','num_trades','taker_base_vol','taker_quote_vol', 'ignore']
                prices.index = [dt.fromtimestamp(x/1000.0) for x in prices.close_time]
                data[i] = prices['close'].astype(float)
                returns[i] = np.append(data[i][1:].reset_index(drop=True)/data[i][:-1].reset_index(drop=True) - 1 , 0)
                self.logger.info(f'[SUCCESS] {i} data downloaded.')
            except:
                self.logger.exception(f'[ERROR] Unable to fetch data for symbol: {i}')
        self.logger.info(f'[COMPLETE] Close prices for following symbols have been downloaded and stored: {symbols}')
        
        return data, returns
    

    def place_market_order(self,client, symbol, side, order_type, quantity):

        self.logger.info(f'[START] Initiating trade order: Symbol: {symbol}; Quantity: {quantity}; Side: {side}; Type: {order_type}')
        try:
            order = client.order_market_buy(symbol=symbol,
                                    side=side,
                                    type=order_type,
                                    quantity=quantity)
            self.logger.info(f'[COMPLETE] Order placed.')
        except:
            self.logger.exception('[ERROR] Unable to place order.')
            exit(1)
        
        return order
    
    def get_order_info(self, client, order):

        symbol = order['symbol']
        orderId = order['orderId']
        self.logger.info(f'[START] Retrieving information for ID: {orderId} ')
        try:
            info = client.get_order(symbol=symbol, orderId=orderId)
            self.logger.info(f'[COMPLETE] Order {orderId} information retrieved.')
        except:
            self.logger.exception('[ERROR] Unable to find trade.')

        return info