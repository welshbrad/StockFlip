import Utils
import Portfolio as pf

'''
Represents Singleton of company listing of information and exchange between Utils API functions.
'''

'''
Set the static companies dataframe
'''
stocks = {}
available_symbols_list = []

def get_available_symbols():
	return available_symbols_list

def get_stock(symbol):
	if symbol in stocks:
		return stocks[symbol]
	
	stock = Utils.get_stock(symbol).get_quote()
	stocks[symbol] = stock
	
	#Change return from 'stock' to 'stocks[symbol]' if we encounter a memory copy issue
	return stock

def update_company_information():
	global available_symbols_list 
	available_symbols_list = Utils.get_symbols()
	symbols_to_update = list(pf.owned_stocks.keys()) + pf.quick_access_companies
	
	for symbol in symbols_to_update:
		if symbol in available_symbols_list:
			stocks[symbol] = Utils.get_stock(symbol).get_quote()

	print("Data updated")	

