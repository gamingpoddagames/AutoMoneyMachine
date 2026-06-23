import sqlite3

connection = sqlite3.connect("data/database.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS news(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT UNIQUE,
    link TEXT,
    published TEXT
)
""")

connection.commit()
connection.close()

print("Database Ready")
