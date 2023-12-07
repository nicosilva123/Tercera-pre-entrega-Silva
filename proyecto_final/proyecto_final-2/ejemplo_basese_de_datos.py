import sqlite3

conn = sqlite3.connect('example.sqlite3')

cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, nombre TEXT, edad INTEGER)''')

cursor.execute("INSERT INTO users (nombre, edad) VALUES ('nicolas',19)")

conn.commit()

cursor.execute("SELECT * FROM users")

filas = cursor.fetchall()
for fila in filas:
    print(fila)
    
conn.close()