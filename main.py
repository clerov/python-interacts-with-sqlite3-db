import sqlite3

# Creating a table to store values

def create_table():
  connection=sqlite3.connect('database.db')
  cursor=connection.cursor ()

  cursor.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

  connection.commit()
  connection.close()

# Inserting vlaues to the table

def insert_values(item, quantity, price):
  connection=sqlite3.connect('database.db')
  cursor=connection.cursor ()

  cursor.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity, price))

  connection.commit()
  connection.close()

# Displaying values which stored in table (database)

def view_values():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor ()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    connection.close()
    print(rows)

# Deleting values in the database

def delete_values(item):
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor ()
    cursor.execute("DELETE FROM store WHERE item=?",(item,))
    connection.commit()
    connection.close()

# Updating values of custom items in database

def update_values(quantity, price, item):
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor ()
    cursor.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
    connection.commit()
    connection.close()

# Test the code 

try:
	create_table()
	view_values()
	update_values(99, 1.2, "Java Dev Guide")
	# try:
	#   insert_values('Java Dev Guide',10,  99.9)
	# except TypeError as err:
	#   print(f'Error: {err}')
except AttributeError as err:
	print(f'Error: {err}')


