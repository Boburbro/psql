import psycopg2

from scr.utils.utils import check_func


class PSQLTableData:
    @check_func
    def __init__(self, user: str, dbname: str,
        host: str="localhost",
        password: str="postgres",
        port: int=5432,
    ):
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        self.cur = self.conn.cursor()

    @check_func
    def addData(self, table_name: str, columns: str, values: tuple):
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({', '.join(['%s'] * len(values))});"
        self.cur.execute(query, values)
        self.conn.commit()
    