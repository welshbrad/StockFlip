from collections import defaultdict
import json
import Utils
import Companies
import threading

trade_lock = threading.Lock()

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

"""
Uses number of credits plus the value of each stock owned to determine total value of portfolio. Returns a float
"""
def calculate_total_value():
	total_value = 0
	for symbol in owned_stocks:
		total_value += (Companies.get_latest_price(symbol) * owned_stocks[symbol])
	total_value += num_credits
	return total_value

total_value = calculate_total_value()

"""
Accessor for the owned_stocks dictionary. Performs existence of symbol check to save code in caller functions and for safety
"""
def get_num_owned(symbol):
	if symbol in owned_stocks:
		return owned_stocks[symbol]
	return 0


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
		global owned_stocks
		if symbol in owned_stocks:
			owned_stocks[symbol] += quantity
		else:
			owned_stocks[symbol] = quantity
	except KeyError as e:
		raise e
		print("KeyError: " + e)
		return False
	return True


'''
Set the quantity of owned stock equal to the old quantity - [quantity] at key [symbol]
Returns True if successful, else False
'''
def remove_stock(symbol, quantity):
	if not (isinstance(symbol, str) and (isinstance(quantity, int))):
		return False
	try:
		global owned_stocks
		if symbol not in owned_stocks:
			return False
		owned_stocks[symbol] -= quantity
	except KeyError as e:
		raise e
		print("KeyError: " + e)
		return False
	if owned_stocks[symbol] == 0:
		del owned_stocks[symbol]
	return True


"""
Triggered by the UI, initiate a buy request, adds stock if user has the sufficient funds. Also makes sure prices are current.
"""
def buy(symbol, quantity):
	global num_credits
	num_credits = float(num_credits)
	quantity = float(quantity)
	price_per = Companies.get_latest_price(symbol)
	old_num_credits = num_credits
	total_price = round(float(quantity) * float(price_per), 2)

	if total_price > num_credits:
		return False, "Not enough credits."
	else:
		ret = 0
		credits_after_buy = num_credits - total_price
		if credits_after_buy < 0:
			return False, ''
		trade_lock.acquire()
		try:
			num_credits = credits_after_buy
			ret = add_stock(symbol, int(quantity))
		finally:
			trade_lock.release()
			if ret:
				return True, ''
			else:
				num_credits = old_num_credits
		return False, "Error"
	
"""
Triggered by the UI, initiate a buy request, removes stock and adds to num_credits if the user has enough shares to complete the request. 
Also makes sure prices are current.
"""
def sell(symbol, quantity):
	global num_credits
	quantity = float(quantity)
	num_credits = float(num_credits)
	price_per = Companies.get_latest_price(symbol)
	old_num_credits = num_credits
	total_price = total_price = round(float(quantity) * float(price_per), 2)

	if symbol not in owned_stocks or quantity > owned_stocks[symbol]:
		return False, "You can't sell what you don't have"
	else:
		ret = 0
		credits_after_sell = num_credits + total_price
		if credits_after_sell < num_credits:
			return False, ''
		trade_lock.acquire()
		try:
			num_credits = credits_after_sell
			ret = remove_stock(symbol, int(quantity))
		finally:
			trade_lock.release()
			if ret:
				return True, ''
			else:
				num_credits = old_num_credits
	return False, "Error"

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


"""
From create account screen, set up new database table
"""
def create_user():
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