import sqlite3

conn = sqlite3.connect("customer.db")
courser = conn.cursor()


# query and fetchall
courser.execute("SELECT * FROM customers")
itemes = courser.fetchall()
print("Name" + "\t\tEmail")
print("-------\t\t--------")
for i in itemes:
    print(i[0] + " " + i[1] + "\t" + i[2])



# Query The Database - ORDER BY DESC or ASC
courser.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")
#courser.execute("SELECT rowid, * FROM customers ORDER BY last_name")
#courser.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
itemes = courser.fetchall()
for items in itemes:
     print(items)



# Limiting the RESULTS
courser.execute("SELECT rowid, * FROM customers LIMIT 2 ")
# the last two
#courser.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2 ")
itemes = courser.fetchall()
for items in itemes:
     print(items)
