from collections import defaultdict
import json
import Utils
import Companies


'''
This is the data for the logged-in user that is loaded from the db. It contains things like balance, owned stocks, and some functions to 
add/remove stocks for a given company
'''
owned_stocks = {}
quick_access_companies = []
username = ''
num_credits = 0
total_value = 0

'''
Add a str(symbol) to the list of quick access companies. to_beginning simply adds it to the front instead of the end.
'''
def add_to_quick_access(symbol, to_beginning=False):
	if not isinstance(symbol, str) or len(quick_access_companies) >= 50:
		print("Symbol not an instance of a string")
		return False
	if to_beginning:
		quick_access_companies.insert(0, symbol)
	else:
		quick_access_companies.append(symbol)
	return True

def calculate_total_value():
	total_value = 0
	for symbol in owned_stocks:
		total_value += (Companies.get_price(symbol) * owned_stocks[symbol])
	total_value += num_credits
	return total_value

total_value = calculate_total_value()


'''
Set the stock to [quantity] at key value [symbol], independent of previous value
Returns True on success, else False
'''
def set_stock(symbol, quantity):
	try:
		owned_stocks[symbol] = quantity
	except KeyError as e:
		raise e
		print("KeyErrorL " + e)
		return False

	assert owned_stocks[symbol] >= 0
	return True


'''
Set the quantity of owned stock equal to the old quantity + [quantity] at key [symbol]
Returns True if successful, else False
'''
def add_stock(symbol, quantity):
	if not (isinstance(symbol, str) and (isinstance(quantity, int))):
		return False
	try:
		owned_stocks[symbol] += quantity
	except KeyError as e:
		raise e
		print("KeyError: " + e)
		return False
	assert owned_stocks[symbol] >= 0
	return True


'''
Set the quantity of owned stock equal to the old quantity - [quantity] at key [symbol]
Returns True if successful, else False
'''
def remove_stock(symbol, quantity):
	owned_stocks[symbol] -= quantity
	assert owned_stocks[symbol] >= 0


'''
Load a user using SQLlite
'''
def load_user(username):
	pass


'''
Dump pf and user data into an SQLlite file
'''
def dump_user_data():
	pass


def reset():
	global owned_stocks
	global quick_access_companies
	global num_credits
	global total_value
	owned_stocks = {}
	quick_access_companies = []
	num_credits = 0
	total_value = 0