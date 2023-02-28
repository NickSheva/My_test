import sqlite3 as sq
with sq.connect('luxary_db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS whatch(
    ''')