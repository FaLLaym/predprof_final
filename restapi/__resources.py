from flask import (Response, Blueprint, send_from_directory)
import os

bp = Blueprint("resources", __name__, static_folder=os.path.join("..", "frontend"))

@bp.route('/js/<script_name>')
def js_resource(script_name) -> Response:
    return send_from_directory(os.path.join(bp.static_folder,"js"), script_name)

@bp.route('/css/<style_name>')
def css_resource(style_name) -> Response:
    return send_from_directory(os.path.join(bp.static_folder, "css"), style_name)

@bp.route('/img/<img_name>')
def css_resource(img_name) -> Response:
    return send_from_directory(os.path.join(bp.static_folder, "img"), img_name)
