from backend.utils.db.db_controller import (points_DB)

from flask import (Response, abort, request, 
                   Blueprint, send_from_directory)
from flask_restful import Resource
import os
import json

class REST_API:
    class Points:
        class GetPoints(Resource):
            def get(self) -> Response:
                return Response(json.dumps(points_DB.get_points()), 200)
