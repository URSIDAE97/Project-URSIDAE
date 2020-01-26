from flask import Blueprint, jsonify, request, redirect
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import safe_str_cmp

from memory import hippocampus
# from memory.model.superior_master import SuperiorMaster
from config import Config


auth_api = Blueprint('auth_api', __name__)


# -- initialize jwt authentication for application -- #
def initialize_security(app):
    app.register_blueprint(auth_api)
    app.config['JWT_SECRET_KEY'] = Config.JWT_KEY
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

    jwt = JWTManager(app)
    jwt.unauthorized_loader(unauthorized_redirect)
    jwt.invalid_token_loader(unauthorized_redirect)
    return jwt


# -- endpoint for authentication purposes -- #
@auth_api.route('/auth', methods=['POST'])
def authenticate():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    if not safe_str_cmp(username, 'test') or not safe_str_cmp(password, 'test'):
        return jsonify({"msg": "Bad username or password"}), 401

    # Identity can be any data that is json serializable
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token), 200


# -- register new master -- #
@auth_api.route('/register', methods=['POST'])
def register_new_master():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    master_name = request.json.get('name', None)
    password = request.json.get('password', None)
    if not master_name:
        return jsonify({"msg": "Missing name parameter"}), 400
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    return jsonify({"msg": "ta da"}), 200


# -- redirects to base url -- #
def unauthorized_redirect(msg):
    print(msg)
    return redirect('/', 301)


# def authenticate(username, password):
#     user = get_master_by_name(username)
#     if user and safe_str_cmp(user.password, password):
#         return user
#
#
# def identity(payload):
#     user_id = payload['identity']
#     return get_master_by_id(user_id)
#
#
# def get_master_by_id(id_master):
#     for user in users:
#         if user.id == id_master:
#             return user
#     return None
#
#
# def get_master_by_name(username):
#     for user in users:
#         if user.username == username:
#             return user
#     return None
