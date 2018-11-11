import sqlite3

conn = sqlite3.connect('user.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users (
        username text, 
        owned_stocks text,
        quick_access_companies text,
        num_credits integer,
        total_value double
        )""")
    

def insert_user(users):
    with conn:
        c.execute("INSERT INTO users VALUES 
                 (:username, :owned_stocks, :quick_access_companies, :num_credits, :total_value)", 
                 {'username': users.username, 'owned_stocks': users.owned_stocks,
                 'quick_access_companies': users.quick_access_companies,
                 'num_credits': users.num_credits, 'total_value': users.total_value})
    
def get_user_by_name(username):
    c.execute("SELECT * FROM users WHERE username=:username", {'username': username}) 
    return c.fetchall()     

def update_quick(quick_access_companies):
    with conn:
        c.execute("""UPDATE users SET quick_access_companies = :quick_access_companies
                  WHERE username = :username""", {'username': users.username,})
        
def update_num_credits(num_credits):
    with conn:
        c.execute("""UPDATE users SET num_credits = :num_credits
                  WHERE username = :username""", {'username': users.username,})

def update_total_value(total_value):
    with conn:
        c.execute("""UPDATE users SET total_value = :total_value
                  WHERE username = :username""", {'username': users.username,})
        
def remove_user(user):
    with conn:
        c.execute("Delete from users WHERE username = :username, {'username': users.username,})


conn.close()