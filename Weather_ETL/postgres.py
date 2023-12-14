import psycopg2

class PostgresClient:
    
    def __init__(self, host, dbname, username, password ):
        try:
            self.conn = psycopg2.connect(f"host={host} dbname={dbname} user={username} password={password}")
            self.cur = self.conn.cursor()
            print('Connection Established')
        except psycopg2.Error as e:
            print(e)
        

    def execute_query(self, query, ls = None):
        try:
            self.cur.execute(query, ls)
            self.conn.commit()
            print('Query Executed!')
        except psycopg2.Error as e:
            self.conn.rollback()
            print(ls)
            print(e)

    def connection_close(self): 
        self.conn.close()