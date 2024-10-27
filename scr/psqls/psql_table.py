import psycopg2

from scr.utils.utils import check_func, greenPrint

class PSQLTable:
    @check_func
    def __init__(self, user: str, dbname: str, 
        host: str="localhost",
        password: str="postgres",
        port: int=5432,
    ):
        self.conn = psycopg2.connect(host=host, dbname=dbname, user=user, password=password, port=port)
        self.cur = self.conn.cursor()

    @check_func
    def createTable(self, table_name: str, query: str):
        """
        If you want to use async function you can call asyncCreateTable;
        On this function we don't use `IF NOT EXISTS` 
        So, use carefully please;

        CREATE TABLE {table_name} ({query});
        
        """
        self.cur.execute(f"CREATE TABLE {table_name} ({query});")
        self.conn.commit()
    
    @check_func
    async def asyncCreateTable(self, table_name: str, query: str):
        """
        If you want to use sync function you can call createTable;
        On this function we don't use `IF NOT EXISTS` 
        So, use carefully please;

        CREATE TABLE {table_name} ({query});
        
        """

        self.cur.execute(f"CREATE TABLE {table_name} ({query});")
        self.conn.commit()

    @check_func
    def getTables(self):
        self.cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public';")
        tables = self.cur.fetchall()

        if len(tables) < 5:
            greenPrint(f"Tables [{len(tables)}]")
            for table in tables:
                greenPrint(f"[{tables.index(table)+1}] {table[0]}")
        
        else:
            greenPrint(f"Tables [{len(tables)}/5]")            
            for i in range(5):
                greenPrint(f"[{i+1}] {tables[i][0]}")
                
        
        return [table[0] for table in tables]

    @check_func
    async def asyncGetTables(self):
        self.cur.execute("SELECT tablename FROM pg_tables WHERE schemaname='public';")
        tables = self.cur.fetchall()

        if len(tables) < 5:
            greenPrint(f"Tables [{len(tables)}]")
            for table in tables:
                greenPrint(f"[{tables.index(table) + 1}]{table[0]}")

        else:
            greenPrint(f"Tables [{len(tables)}/5]")
            for i in range(5):
                greenPrint(f"[{i + 1}] {tables[i][0]}")

        return [table[0] for table in tables]

    @check_func
    def deleteTable(self, table:str):
        self.cur.execute(f"DROP TABLE {table};")
        self.conn.commit()
        self.getTables()

    @check_func
    async def asyncDeleteTable(self, table:str):
        self.cur.execute(f"DROP TABLE {table};")
        self.conn.commit()
        self.getTables()

    @check_func
    def renameTable(self, old_name:str, new_name: str):
        self.cur.execute(f"ALTER TABLE {old_name} RENAME TO {new_name};")
        self.conn.commit()
        self.getTables()

    @check_func
    async def asyncRenameTable(self, old_name:str, new_name: str):
        self.cur.execute(f"ALTER TABLE {old_name} RENAME TO {new_name};")
        self.conn.commit()
        self.getTables()

    @check_func
    def close(self):
        self.cur.close()
        self.conn.close()
    
    @check_func
    async def asyncClose(self):
        self.cur.close()
        self.conn.close()


   