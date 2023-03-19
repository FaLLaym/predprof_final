import sqlite3

from backend import (DEBUG, DB_NAME)
from .. import logger

sql, db = None, None

try:
    db = sqlite3.connect(f"./db/{DB_NAME}", check_same_thread=False)
except sqlite3.DatabaseError as e:
    raise e(f"Can't open {DB_NAME}, DB-Name in config.ini seems to be incorrect")

sql = db.cursor()

sql.execute("DROP TABLE IF EXISTS session_data")

sql.execute( #TODO
    f"""CREATE TABLE session_data (
        id INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
        oxygen INTEGER NOT NULL,
        fuel INTEGER UNIQUE NOT NULL,
        money INTEGER NOT NULL
    )""") #TODO

sql.execute("DROP TABLE IF EXISTS points")

sql.execute(
    f"""CREATE TABLE IF NOT EXISTS points (
        id INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
        chunk_id INTEGER NOT NULL,
        sh INTEGER NOT NULL,
        distance INTEGER NOT NULL
    )"""
)

db.commit()

if DEBUG["db"]: logger.debug("DB inited")
