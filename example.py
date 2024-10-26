from psql import PSQL

sql = PSQL(
    user='root',
    dbname='baza'
)
# create table
sql.createTable("users1", "user_id VARCHAR, bio TEXT")
sql.createTable("users2", "user_id VARCHAR, bio TEXT")

# get table on list and print
tables = sql.getTables()

# delete table and print
sql.deleteTable(tables[0])

# get table on list and print
tables = sql.getTables()

# rename table and print
sql.renameTable(tables[0],"_" + tables[0])