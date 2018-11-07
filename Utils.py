import iexfinance as iex
from datetime import datetime
from datetime import timedelta
import pandas as pd
from iexfinance import get_available_symbols
import json
from iexfinance import Stock
import requests_cache

'''
This will create an automatic caching session key, which will be passed into all request functions to cache results
Expiry default is 1 minute
'''
def create_cache_session():
	expiry = timedelta(minutes=15)
	session = requests_cache.CachedSession(cache_name='finance_cache', backend='sqlite', expire_after=expiry)
	assert session is not None
	return session

cache_session = create_cache_session()

'''
Use this as an assertion that a decorated child method
is indeed overriding its parent. 

Usage: add @overrides([parent class name]) before child method
'''
def overrides(interface_class):
    def overrider(method):
        assert(method.__name__ in dir(interface_class))
        return method
    return overrider

'''
NASDAQ company listing, access from API
Returns Pandas dataframe
'''
def get_symbols():
	company_list = iex.get_available_symbols(session = cache_session)
	symbol_list = []
	for company in company_list:
		symbol_list.append(company['symbol'])
	return symbol_list

'''
Use code, (e.g. AAPL) and a time slice to get data from iexfinance API
Returns Pandas dataframe
'''    
def get_company_data_start_end(company_code, start, end):
	#here, make a call to the api using a company code 
	df = iex.get_historical_data(company_code, start=start, end=end, output_format='json')
	return df

"""
Use code, (e.g. AAPL) to get data from iexfinance API from one minute ago until now
Returns Pandas dataframe
"""
def get_company_data_time_delta(company_code):
	#get current time (end)
	#now = datetime.now()
	#start = now - timedelta(minutes=time_delta)
	start = datetime.strptime("01-06-2018", "%d-%m-%Y")
	end = datetime.strptime("02-06-2018", "%d-%m-%Y")
	data_list = iex.get_historical_data(company_code, start=start, end=end, output_format="pandas", session=cache_session)
	return data_list

"""
Yields the stock endpoint from the iexfinance iAPI, caches data
"""
def get_stock(company_code):
	stock_reader = Stock(company_code, output_format='json', session=cache_session)
	return stock_reader


#print(iex.get_historical_data("AAPL", start, end, output_format='pandas'))