## INTRODUCTION
The fact table "songplays" and dimension tables "users", "songs", "artists", "time" were created and saved to the PostgreSQL database. An ETL pipeline was created to extract, transform, and load JSON data into tables. 

## FILES IN PROJECT

| FILE NAME  	| CONTENT 	|
|---		|---	|	
|   sql_queries.py	| SQL queries in PostgreSQL, including create/drop tables, insert records, find songs	| 
|   create_tables.py	|   Connect to PostgreSQL, create database, create tables by quering SQL from sql_queries.py 	| 
|   etl.ipynb	|   Notebook to visualize results from building the ETL process 	| 
|   etl.py	|   Based on etl.ipynb, process ETL on the entire datasets   	| 
|   test.ipynb | Test your work | 

## INSTRUCTION
```bash
project/
├── create_tables.py
├── etl.ipynb
├── etl.py
├── README.md
├── sql_queries.py
└── test.ipynb
```

### CREATE TABLES
**Create_tables.py** 
1. Import functions create tables from sql_queries.py
2. Connect to the pyscopg2 database with host=127.0.0.1, dbname=studentdb, user=student, password=student
3. Create our database named sparkifydb (drop database if exists)
4. Create our tables to load data (drop tables if exists)
5. Write CREATE statements in sql_queries.py to create each table
6. Write DROP statements in sql_queries.py to drop each table if it exists
7. Disconnect to the pyscopg2 database

**ETL.ipynb**
8. Run create_tables.py to create your database and tables

**Test.ipynb**
Run test to confirm the table creation

### BUILDING ETL PIPELINE 
*NOTE: Always rerun create_tables.py to reset your tables before running the ETL.ipynb notebook*

**ETL.ipynb**
1. Connect to the sparkifydb database
2. Read JSON files in pandas dataframe
3. Extract data (select columns) from pandas dataframes, and insert data into tables which have been
4. Disconnect to the sparkifydb database
5. Run sanity tests in test.ipynb







