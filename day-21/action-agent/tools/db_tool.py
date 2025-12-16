import sqlite3

def db_query(query: str):
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows