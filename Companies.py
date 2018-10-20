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


'''
Use this to display buttons for each company list
'''
def display_company_list():
	print(companies.head())


