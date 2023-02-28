import sqlite3 as sq
with sq.connect('venv/clients.db') as con:
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS clients (
    first_name TEXT,
    last_name TEXT,
    product,
    number,
    reference,
    date_pledge,
    sum,
    percentage,
    prolongation)
    ''')