import sqlite3

conn = sqlite3.connect("customer.db")
courser = conn.cursor()
# insert one record into the Table
courser.execute("INSERT INTO customers VALUES('Anton', 'Serbezov', 'anton.serbezov@icloud.com')")

########################################
# insert many records in the table
many_records = [
     ("Geralt", "Rivia", "witcher@we.com"),
     ("Ragnar", "Lothbrokk", "viking@we.com"),
     ("John", "Cena", "wwe@br.com"),
     ("Stanimira", "Argirova", "stan@we.com"),
     ("Geri", "Bocheva", "geri@we.com"),
]
# # # ? place holder for SQL lite
courser.executemany("INSERT INTO customers VALUES(?,?,?)", many_records)

###########################################

# query and fetchall
courser.execute("SELECT * FROM customers")
#print(courser.fetchone())
#print(courser.fetchone()[0])
#print(courser.fetchmany(3))
print(courser.fetchall())

# commit our command
conn.commit()

#Close our connection
conn.close()
