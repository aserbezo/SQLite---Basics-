import sqlite3


conn = sqlite3.connect("customer.db")
courser = conn.cursor()

# Update Records
courser.execute("""UPDATE customers SET first_name = "Tony"
                    WHERE last_name = 'Serbezov'
 """)
# make updates using a rowid
courser.execute("""UPDATE customers SET first_name = "Anton"
                    WHERE rowID = 1
 """)
conn.commit()
# Query the Database
courser.execute("SELECT rowid, * FROM customers")
itemes = courser.fetchall()
for items in itemes:
     print(items)


# Delete Records
courser.execute("DELETE FROM customers WHERE rowid = 4")
conn.commit()
courser.execute("SELECT rowid, * FROM customers")
itemes = courser.fetchall()
for items in itemes:
     print(items)
