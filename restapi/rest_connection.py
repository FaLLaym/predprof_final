from backend.utils.db.db_controller import (points_DB, session_DB)

from flask import (Response, abort, request, 
                   Blueprint, send_from_directory)
from flask_restful import Resource
import os
import json

class REST_API:
    class Session:
        class PassSession(Resource):
            def get(self) -> Response:
                args = request.args #BUG

                oxygen = args["oxygen"]
                fuel = args["fuel"]
                money = args["money"]

                inited_status = session_DB.init_session(oxygen, fuel, money)
                if inited_status == 400:
                    abort(Response("session is already created", 400))

                return Response("session created", 200)
            
        class GetSession(Resource):
            def get(self) -> Response:
                session = session_DB.get_session()

                if not session:
                    abort(Response("session is not created", 400))

                return Response({"session": {"oxygen": session[0], "fuel": session[1], "money": session[2]}}, 200)

    class Points:
        class GetPoints(Resource):
            def get(self) -> Response:
                return Response(json.dumps(points_DB.get_points()), 200)
