import sqlite3

conn = sqlite3.connect("assets.db")
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in assets.db:", tables)

conn.close()
