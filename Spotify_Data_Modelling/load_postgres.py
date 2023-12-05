import psycopg2
import pandas as pd 
import config 
import queries

def gloabl_create_database(dbname):
    try:
        conn = psycopg2.connect(f"host={config.HOST} dbname={config.GLOBAL_DBNAME} user={config.USERNAME} password={config.PASSWORD}")
        conn.set_session(autocommit=True)
        cur = conn.cursor()

        cur.execute(f"DROP DATABASE {dbname}")
        print('Drop Statement Executed!')
        cur.execute(f"CREATE DATABASE {dbname}")
        print('Create Statement Executed!')

        conn.close()
        
        print('Create Database Function Executed!')
    except psycopg2.Error as e:
        print(e)
        return False

def create_connection(dbname):
    try:
        conn = psycopg2.connect(f"host={config.HOST} dbname={dbname} user={config.USERNAME} password={config.PASSWORD}")
        cur = conn.cursor()
        print('Create Database Function Executed!')
        return conn, cur
    except psycopg2.Error as e:
        print(e)
        return None, None

# PART 1: Create Database
cmd_executed = gloabl_create_database(config.DBNAME)
if cmd_executed:
    conn, cur = create_connection(config.DBNAME)
    conn.close()

# PART 2: Create Tables
def execute_query(conn, cur, query, ls = None):
    try:
        cur.execute(query, ls)
        conn.commit()
        print('Query Executed!')
    except psycopg2.Error as e:
        conn.rollback()
        print(ls)
        print(e)

conn, cur = create_connection(config.DBNAME)

create_queries = queries.create_queries
for create_key, create_query in create_queries.items():
    print(create_query)
    execute_query(conn, cur, create_query)

# PART 3: Insert Into Tables
insert_queries = queries.insert_queries
data_folder_path = "data"
for insert_key, insert_query in insert_queries.items():
    filename = f"{data_folder_path}/{insert_key}.csv"
    print(f"Processing CSV File {filename}")

    temp_df = pd.read_csv(filename)
    print(insert_query)

    for idx, row in temp_df.iterrows(): 
        execute_query(conn, cur, insert_query, list(row))

conn.close()