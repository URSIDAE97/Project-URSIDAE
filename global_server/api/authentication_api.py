from flask import Blueprint, request, jsonify
from service import SecurityService
from .error_codes import missing_request_body, missing_required_parameters, unauthorized


authentication_api = Blueprint('authentication_api', __name__)


@authentication_api.route('/login', methods=['POST'])
def authenticate_user():
    """
    Authenticate user
    """
    if not request.is_json:
        return missing_request_body()

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not (username and password):
        return missing_required_parameters()

    ss = SecurityService()
    access_token = ss.authenticate_user(username, password)
    if access_token:
        return jsonify(access_token=access_token), 200
    else:
        return unauthorized()
