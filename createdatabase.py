import psycopg2
conn = psycopg2.connect(
            host = 'localhost',
            database = 'postgres',
            user = 'postgres',
            password = 'bavya2007',
            port = '5432'
        )

conn.autocommit = True

cursor = conn.cursor()

cursor.execute("CREATE DATABASE fee_porject")
cursor.close()
conn.close()

print("database created")

