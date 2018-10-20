import iexfinance as iex
from datetime import datetime
from datetime import timedelta
import pandas as pd
from iexfinance import get_available_symbols
import json

time_delta = 60

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
	df = iex.get_historical_data(company_code, start=start, end=now, output_format="pandas")
	return df



symbols = get_symbols()
print(symbols.head())

start = datetime(2018, 9, 20)
end = datetime(2018, 10, 20)

for symbol in symbols:
	print(get_company_data_start_end(symbol.loc(), start, end))