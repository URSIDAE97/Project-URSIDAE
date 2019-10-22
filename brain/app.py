from flask import Flask, render_template

from api import *
from services import security
from memory import hippocampus

app = Flask(__name__)
app.register_blueprint(test_api)

jwt = security.initialize_security(app)
hippocampus.initialize_memory(app)


@app.route('/', methods=['GET'])
def info_page():
    return render_template('unauthorized.html'), 401


@app.errorhandler(404)
def route_not_found(msg):
    return security.unauthorized_redirect(msg)


if __name__ == '__main__':
    app.run(port=5656, debug=True)
