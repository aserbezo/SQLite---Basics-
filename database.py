import sqlite3


# Query THE DB and Return all records
def show_all():
    # connect to database
    conn = sqlite3.connect("customer.db")
    # create a cursor
    cursor = conn.cursor()
    # Query The Database
    cursor.execute("SELECT rowid, * FROM customers")
    items = cursor.fetchall()
    for items in items:
        print(items)

    conn.close()


# add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


# Delete Record from table
def delete_one(id):
    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()
    cursor.execute("DELETE from customers WHERE rowid = (??)", id)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


# add many records to Table
def add_many(list):
    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()
    cursor.executemany("INSERT INTO customers VALUES (?,?,?)", list)
    # commit our command
    conn.commit()
    # close our connection
    conn.close()


# Lookup with Where
def email_lookup(email):
    conn = sqlite3.connect("customer.db")
    cursor = conn.cursor()
    # (email,) it s tuple
    cursor.execute("SELECT * from customers WHERE email = (?)", (email,))
    items = cursor.fetchall()
    for items in items:
        print(items)
    conn.commit()
    conn.close()
