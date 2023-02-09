import sqlalchemy as db
from sqlalchemy import MetaData, Table, Column, Integer, ARRAY, Date, Text, \
    REAL

engine = db.create_engine('sqlite:///local_db_1.db')
connection = engine.connect()
metadata = MetaData()

data = Table('data', metadata,
             Column('id', Integer(), primary_key=True),
             Column('date', Date),
             Column('trans', Text()),
             Column('qty', Integer()),
             Column('price', REAL())
             )

metadata.create_all(engine)

query_0 = (db.insert(data).values(id="9", trans="BUY"))
query = data.insert().values(trans = "BUY", qty = "100", price = 123, id = 12 )


print(query)

connection.execute(query_0)
connection.execute(query)

# Required for sqlalchemy 2.0
# connection.commit()