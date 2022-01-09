import sqlite3

conn = sqlite3.connect("customer.db")
courser = conn.cursor()


#Primary keys unique number for record in database
courser.execute("SELECT rowid, * FROM customers")
itemes = courser.fetchall()
for items in itemes:
    print(items)

#where clause , how to search things , we also can use >= 21 if there is a numbers
#we could use LIKE  example  WHERE last_name LIKE 'Ser%'

courser.execute("SELECT * FROM customers WHERE last_name = 'Serbezov'")
itemes = courser.fetchall()
for items in itemes:
    print(items)

# Query The Database - AND / OR, when we're using AND the both conditions  its need to be TRUE , with OR only one conditions is need to be true
courser.execute("SELECT rowid, * FROM customers WHERE last_name LIKE 'Ser%' OR rowid = 1 ")
itemes = courser.fetchall()
for items in itemes:
     print(items)
