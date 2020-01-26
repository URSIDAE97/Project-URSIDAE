from flask import Flask, render_template

from api import *
from services import security
from memory import database

app = Flask(__name__)
app.register_blueprint(test_api)

database.initialize_memory(app)
jwt = security.initialize_security(app)


@app.route('/', methods=['GET'])
def info_page():
    return render_template('index.html'), 401


@app.errorhandler(404)
def route_not_found(msg):
    return security.unauthorized_redirect(msg)


if __name__ == '__main__':
    app.run(port=6969, debug=True)
