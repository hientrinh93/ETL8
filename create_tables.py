import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """returns cursor and connection to the sparkifydb database. 

    This function connects to the default database "studentdb" in PostgreSQL to create the 
    "sparkifydb" database (or drop the "sparkifydb" database if it exists)
    
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    This function drops each table using the queries in `drop_table_queries` list.

    - **parameters**::

          :param cur: cursor from the connection
          :param conn: connection to the "sparkifydb" database
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    This function creates each table using the queries in `create_table_queries` list.

    - **parameters**::

          :param cur: cursor from the connection
          :param conn: connection to the "sparkifydb" database

    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    Executes drop_tables and create_tables functions and closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()