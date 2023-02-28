import sqlite3 as sq
with sq.connect('venv/table.db') as con:
    cur = con.cursor()

    cur.execute('''INSERT INTO watch(number, ref, name, sale, date_info) VALUES(%s, %s)''',
                ("345UI89", "GER4564433", "Omega", "200000", "10-02-2023")