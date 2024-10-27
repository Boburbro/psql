
from scr.psql import PSQL


sql = PSQL(user="bobur", dbname="test")

sql.getTables()

sql.createTable("test1", "text TEXT, text1 TEXT")

sql.addData('test1', 'text, text1', ("salom", "alik"))