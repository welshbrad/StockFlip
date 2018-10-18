import iexfinance as iex
from datetime import datetime
from datetime import timedelta
import pandas
from iexfinance import get_available_symbols


time_delta = 1000 * 60

'''
NASDAQ company listing, access from API
'''
def get_company_list():
    pass
    #nasdaq company information. Return as a list 

'''
Use code, (e.g. AAPL) and a time slice to get data from iexfinance API
Returns Pandas dataframe
'''    
def get_company_data_start_end(company_code, start, end):
    #here, make a call to the api using a company code: ex 
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

def get_symbols():
    company_list = get_available_symbols(output_format='pandas')
    return company_list


#print(get_company_data_start_end("AAPL", datetime(2017, 2, 9),  datetime(2017, 5, 24)))
#print(get_company_data_time_delta("AAPL"))
symbols = get_symbols()
for symbol in symbols:
    print("Company: ", symbol['name'])



print("Done")
