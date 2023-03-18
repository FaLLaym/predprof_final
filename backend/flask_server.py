import logging
from flask import (Flask, Response, abort, request, send_from_directory)
# from flask_cors import CORS
from flask_restful import Api
import os

from restapi import (rest_connection, __resources)
from . import (DEBUG, TOKEN)
from restapi.rest_connection import REST_API

app = Flask(__name__, static_folder=os.path.join("..", "frontend"))
# CORS(app)

app.register_blueprint(__resources.bp)

api = Api(app)

api.add_resource(REST_API.Test, "/api/test/<string:test_string>", endpoint="test")

@app.route('/', methods=["GET"])
def index() -> Response:
    return send_from_directory(app.static_folder, "index.html")

@app.route("/<page>", methods=["GET"])
def page_render(page) -> Response:
    return send_from_directory(app.static_folder, page)

def main(port) -> None:
    DEBUG_BACKEND = DEBUG["backend"]
    
    if DEBUG_BACKEND:
        log = logging.getLogger("werkzeug")
        log.disabled = True
        app.logger.disabled = True

    app.run(debug=DEBUG_BACKEND, port=port)
