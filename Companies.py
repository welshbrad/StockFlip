import Utils as utils

'''
Represents Singleton of company listing of information and exchange between Utils API functions.
'''

'''
Set the static companies dataframe
'''
def init_companies():
	companies = utils.get_symbols()
	return companies

companies = init_companies()

def get_company_information(symbol):
	pass
	


