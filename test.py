# import psycopg2 as sql

# #inital
# conn = sql.connect(host="localhost", dbname="test", user="bobur", password="postgres", port=5432)
# cur = conn.cursor()

# cur.execute("""
#     CREATE TABLE IF NOT EXISTS users (
#         id SERIAL PRIMARY KEY, 
#         name VARCHAR(255)
#     )
# """)

# # end
# conn.commit()
# cur.close()
# conn.close()


from psql import PSQL 

sql = PSQL(user="bobur", dbname="test")

sql.getTables()
# sql.renameTable("_a2sks", '_asks')
sql.deleteTable("*")