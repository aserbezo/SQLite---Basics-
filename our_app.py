import database

# add a record to the database
#database.add_one("Tony","SERBEZOV","djakito89@gmail.com")

# add many records to the table

# stuff = [
#     ('lili','Brown','lili@we.com'),
#     ('gocho','Milk','go@we.com'),
#     ('mike','Low','mike@we.com')
#     ]
# database.add_many(stuff)

# Lookup Email Address Record
database.email_lookup("anton.serbezov@icloud.com")


# delete a record from to the database and use rowid as string with two digits number like 21, 22 we get error
#database.delete_one('9')

# show all the record
#database.show_all()
