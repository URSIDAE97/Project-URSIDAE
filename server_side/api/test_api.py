from flask import Blueprint
from flask_jwt_extended import jwt_required
from services import TestService


test_api = Blueprint('test_api', __name__)


@test_api.route('/test')
@jwt_required
def test():
    return 'test passed'


@test_api.route('/test2')
def test2():
    return 'test passed'


@test_api.route('/test3')
def test3():
    ts = TestService()
    result = ts.db_test()
    return result
