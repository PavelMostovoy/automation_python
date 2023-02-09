import sqlite3

con = sqlite3.connect('local_db.db')


cur = con.cursor()

# Create table
table_name = "secondary"
query = f"CREATE TABLE if not exists {table_name} (date text, trans text, id real, qty real, price real)"

cur.execute(query)



# sql_request = '''CREATE TABLE secondary
#                (date text, trans text, id real, qty real, price real)'''

# cur.execute(sql_request)

# Insert a row of data
cur.execute(f"INSERT INTO secondary VALUES ('2006-01-07','BUY','RHAT',100,35.14)")


# Save (commit) the changes
con.commit()


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.

for row in cur.execute('SELECT * FROM data ORDER BY date'):
    print(row)

con.close()
