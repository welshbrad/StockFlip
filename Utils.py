import iexfinance as iex
from datetime import datetime
from datetime import timedelta
import pandas as pd
from iexfinance import get_available_symbols
import json
from iexfinance import Stock
import requests_cache
import Companies

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

	company_info = {}
	for company in company_list:
		company_info[company['symbol']] = company['name']
	return company_info

'''
Use code, (e.g. AAPL) and a time slice to get data from iexfinance API
Returns Pandas dataframe
'''    
def get_company_data_start_end(company_code, start, end):
	#here, make a call to the api using a company code 
	df = iex.get_historical_data(company_code, start=start, end=end, output_format='json')
	return df


"""
Yields the stock endpoint from the iexfinance iAPI, caches data
"""
def get_stock(company_code):
	if not isinstance(company_code, str):
		raise TypeError('company_code should be a str.')
		return False
	
	stock_reader = Stock(company_code, output_format='json', session=cache_session)
	return stock_reader


"""
Gives the LATEST stock quote, ignoring all cached data 
"""
def get_latest_stock_quote(company_code):
	if not isinstance(company_code, str):
		raise TypeError("Company_code should be a string.")
		return False
	stock_reader = Stock(company_code, output_format='json').get_quote()
	return stock_reader

"""
Returns all the conveniently formatted data from the API which will be used for charting. 
"""
def get_chart_data(company_code):
	stock_reader = Stock(company_code, output_format='json', session=cache_session)
	chart_dict = stock_reader.get_chart()
	return chart_dict

"""
Input a company name (exact text) and return the symbol:
"""
def symbol_from_name(name):
	for key, value in Companies.available_symbols_dict.items():
		if value == name:
			return key
	return None