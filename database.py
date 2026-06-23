import sqlite3

DATABASE = "data/database.db"

def connect():
    return sqlite3.connect(DATABASE)
