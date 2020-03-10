from flask import Blueprint, request
from service import SecurityService


authentication_api = Blueprint('authentication_api', __name__)


@authentication_api.route('/login', methods=['POST'])
def authenticate_user():
    """
    Authenticate user
    """
    data = request.json
    ss = SecurityService()
    result = ss.authenticate_user(data.get('login', ''), data.get('password', ''))
    if result:
        return data, 200
    else:
        return '', 403
