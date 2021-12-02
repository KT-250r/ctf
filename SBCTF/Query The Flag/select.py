#!/usr/bin/python3
import sqlite3

conn = sqlite3.connect('find.db')
c = conn.cursor()

for i in range(300):
    try:
        c.execute(f"select * from falg{i};")
    except:
        continue

    result = c.fetchone()
    print(result)

conn.close()