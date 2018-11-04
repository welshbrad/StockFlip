import iexfinance as iex
from datetime import datetime
from datetime import timedelta
import pandas as pd
from iexfinance import get_available_symbols
import json

time_delta = 60

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
	company_list = iex.get_available_symbols(output_format='pandas')
	company_list = pd.DataFrame(company_list)
	return company_list

'''
Use code, (e.g. AAPL) and a time slice to get data from iexfinance API
Returns Pandas dataframe
'''    
def get_company_data_start_end(company_code, start, end):
	#here, make a call to the api using a company code 
	df = iex.get_historical_data(company_code, start=start, end=end, output_format='pandas')
	return df


"""
Use code, (e.g. AAPL) to get data from iexfinance API from one minute ago until now
Returns Pandas dataframe
"""
def get_company_data_time_delta(company_code):
	#get current time (end)
	now = datetime.now()
	start = now - timedelta(minutes=time_delta)
	data_list = iex.get_historical_data(company_code, start=start, end=now, output_format="pandas")
	return data_list
start = datetime.strptime("01-06-2018", "%d-%m-%Y")
end = datetime.strptime("30-06-2018", "%d-%m-%Y")

print(iex.get_historical_data("AAPL", start, end, output_format='pandas'))