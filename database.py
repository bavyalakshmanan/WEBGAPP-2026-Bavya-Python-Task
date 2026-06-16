import psycopg2

# conn = psycopg2.connect(
#     host = 'localhost',
#     database = 'postgres',
#     user = 'postgres',
#     password = 'bavya2007',
#     port = '5432'
# )

# conn.autocommit = True

# cursor = conn.cursor()
# cursor.execute("CREATE DATABASE student_db")
# cursor.close()
# conn.close()
# print("Database Created")

conn = psycopg2.connect(
    host = 'localhost',
    database = 'student_db',
    user = 'postgres',
    password = 'bavya2007',
    port = '5432'
)
cursor = conn.cursor()

# cursor.execute("""
# CREATE TABLE users(
#      id SERIAL PRIMARY KEY,
#      name VARCHAR(100),
#      email VARCHAR(100)    
#                 )
# """)

# cursor.execute(
#     "INSERT INTO users(name,email) VALUES(%s,%s)",
#     ("Hari","hariinfosolutions@gmail.com")
# )

cursor.execute("DELETE FROM users WHERE id = 2")

conn.commit()

cursor.execute("SELECT * FROM users")

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()