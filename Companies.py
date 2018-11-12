import Utils
import Portfolio as pf

'''
Represents Singleton of company listing of information and exchange between Utils API functions.
'''

'''
Set the static companies dataframe
'''
stocks = {}
available_symbols_dict = {}
charts = {}

def get_available_symbols():
	return list(available_symbols_dict.keys())

def get_stock(symbol):
	if symbol in stocks:
		return stocks[symbol]
	
	stock = Utils.get_stock(symbol).get_quote()
	stocks[symbol] = stock
	
	#Change return from 'stock' to 'stocks[symbol]' if we encounter a memory copy issue
	return stock


"""
Will cause lag from the API call. Use only when validating a trade. 
"""
def get_latest_price(symbol):
	try:
		return Utils.get_latest_stock_quote(symbol)["latestPrice"]
	except KeyError:
		print("Symbol not found")

def update_company_information():
	global available_symbols_dict 
	available_symbols_dict = Utils.get_symbols()
	symbols_to_update = list(pf.owned_stocks.keys()) + pf.quick_access_companies

	for symbol in symbols_to_update:
		if symbol in get_available_symbols():
			stocks[symbol] = Utils.get_stock(symbol).get_quote()
			charts[symbol] = Utils.get_chart_data(symbol)
		
