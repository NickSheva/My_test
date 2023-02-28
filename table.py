import sqlite3 as sq
with sq.connect('my_table1.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS items (
    user_id INTEGER PRIMARY KEY,
    name TEXT,
    reference TEXT,
    number TEXT,
    price INTEGER
    )''')
