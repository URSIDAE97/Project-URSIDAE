from flask import Blueprint, redirect

test_api = Blueprint('test_api', __name__)


@test_api.route('/test')
def test():
    return 'test passed'


@test_api.route('/test2')
def test2():
    return redirect('/', 301)
