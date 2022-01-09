import sqlite3


# create connection
# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect("customer.db")

# building a table and create cursor
courser = conn.cursor()
courser.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")


# five Datatypes in SQLite
# NULL
# integer
# Real
# Text
# Blob = images , mp3 files



# Deleting a TABLE
# courser.execute("DROP TABLE customers")
# conn.commit()
# # itemes = courser.fetchall()
# # for items in itemes:
# #     print(items)
# conn.commit()
