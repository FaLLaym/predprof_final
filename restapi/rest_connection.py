from flask import (Response, abort, request, 
                   Blueprint, send_from_directory)
from flask_restful import Resource
import os

class REST_API:
    class Test(Resource):
        def get(self, test_string: str) -> Response:
            return Response(f"This thingy is cool -> {test_string}", 200)
