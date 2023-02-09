import sqlalchemy as db

# with debug
# engine = db.create_engine('sqlite:///local_db.db', echo = True)

engine = db.create_engine('sqlite:///local_db.db')

connection = engine.connect()

metadata = db.MetaData()

data = db.Table('data', metadata , autoload=True, autoload_with=engine)
secondary = db.Table('secondary', metadata, autoload=True, autoload_with=engine)


query = db.select(data.c.price)

received = connection.execute(query)

print(received.fetchone())

query = db.select(data.c.date,).join(secondary, data.c.price <= secondary.c.price)



result = connection.execute(query)

print(result.fetchall())


exit()
# Print the column names

# example for single table
# query = db.select(census.c.date).filter(census.c.qty == 100,
#                                         census.c.trans == "BUY")

query = db.select(data.c.date,).join(secondary, data.c.id == secondary.c.id)

print(query)

received_data = connection.execute(query)
received_data = received_data.fetchall()

print(data)
#
# # Print full table metadata
# print(repr(metadata.tables['stocks']))
#
# #Equivalent to 'SELECT * FROM census'
# query = db.select([census])
# query_1 = db.select([census]).where(census.c.qty == 70)
#
#
# ResultProxy = connection.execute(query_1)
# ResultSet = ResultProxy.fetchall()
# print(ResultSet[:])

# print(metadata)