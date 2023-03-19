from backend import (DEBUG, TOKEN)
from ..db import db_init
from .. import logger
from backend.handlers.api_handler import get_points

from sqlite3 import OperationalError

sql = db_init.sql
db = db_init.db

class session_DB:
    @staticmethod
    def get_session() -> None:
        rows = sql.execute(f"""
            SELECT oxygen, fuel, money FROM session_data
        """).fetchone()

        return rows

    @staticmethod
    def init_session(oxygen: int, fuel: int, money: int) -> int:
        if session_DB.get_session():
            return 400

        sql.execute(f"""
            INSERT INTO session_data (
                oxygen, fuel, money
            ) VALUES (?, ?, ?)""", [oxygen, fuel, money])
        db.commit()
        return 200
    
class points_DB:
    @staticmethod
    def init_points() -> None:
        points_data = get_points()

        for chunk_id, data_chunk in enumerate(points_data):
            for point_data in data_chunk["points"]:
                sql.execute(f"""
                    INSERT INTO points (
                        chunk_id, sh, distance
                    ) VALUES (?,?,?)""", [chunk_id, int(point_data["SH"]), int(point_data["distance"])])
    
        db.commit()

    @staticmethod
    def get_points():
        points = {}
        points_data= sql.execute(f"""
            SELECT chunk_id, sh, distance FROM points
        """).fetchall()

        for point_data in points_data:
            chunkid, sh, distance = point_data

            if not chunkid in points:
                points[chunkid] = []
            
            points[chunkid] += [{"SH": sh, "distance": distance}]
            
        return {"points": points}
