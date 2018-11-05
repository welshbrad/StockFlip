import Utils

'''
Represents Singleton of company listing of information and exchange between Utils API functions.
'''

'''
Set the static companies dataframe
'''

quick_access_data = None 

def init_quick_access_companies(symbol_list):
	quick_access_data = Utils.get_stock(symbol_list)
	return quick_access_data


def get_company_information(symbol):
	pass
	

