import sqlite3
import os
from settings import DBPATH



def schema(dbpath = DBPATH):
    with sqlite3.connect(dbpath) as conn:
        cur = conn.cursor()

        DROPSQL = "DROP TABLE IF EXISTS shirts;"
        cur.execute(DROPSQL)

        SQL = """CREATE TABLE shirts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            style VARCHAR(128),
            size VARCHAR(128),
            color VARCHAR(128))"""
        cur.execute(SQL)


if __name__ == "__main__":
    schema()