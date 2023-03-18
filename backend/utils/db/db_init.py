import sqlite3

from backend import (DEBUG, DB_NAME)
from backend.utils.db import (db_init, db_controller)
from .. import logger

db, sql = None, None

def db_init() -> None:
    try:
        db = sqlite3.connect(f"./db/{DB_NAME}", check_same_thread=False)
    except sqlite3.DatabaseError as e:
        raise e(f"Can't open {DB_NAME}, DB-Name in config.ini seems to be incorrect")

    sql = db.cursor()
    
    sql.execute( #TODO
        f"""CREATE TABLE IF NOT EXISTS test (
            id INTEGER UNIQUE NOT NULL PRIMARY KEY AUTOINCREMENT,
        )""")
    
    db.commit()

    if DEBUG["Debug"]["DB"]: logger.debug("DB inited")
