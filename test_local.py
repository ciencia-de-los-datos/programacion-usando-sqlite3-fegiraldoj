import sqlite3
import sys

import pandas as pd

def load_data():
    conn = sqlite3.connect(":memory:")
    cur = conn.cursor()

    with open("create_tables.sql", encoding="utf-8") as file:
        cur.executescript(file.read())

    return conn, cur

conn, cur = load_data()
with open("pregunta_04.sql", encoding="utf-8") as file:
    query = file.read()

query = "SELECT k0, AVG(c12) FROM tbl1 WHERE c13 > 400 GROUP BY k0;"
for a in cur.execute(query).fetchall():
    print(a)

print(pd.read_sql_query(query, conn).to_dict())

print("terminé")