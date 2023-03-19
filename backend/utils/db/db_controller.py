from backend import (DEBUG, TOKEN)
from ..db import db_init
from .. import logger
from backend.handlers.api_handler import get_points

from sqlite3 import OperationalError

sql = db_init.sql
db = db_init.db

# class session_DB:
#     ...

class points_DB:
    @staticmethod
    def init_points() -> None:
        points_data = get_points()

        for chunk_id, data_chunk in enumerate(points_data):
            print(data_chunk)
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
