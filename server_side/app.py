from flask import Flask
from flask_cors import CORS
from config import Configuration
from model import db, alembic
from api import *


app = Flask(__name__)

"""
configuration
"""
app.config.from_object(Configuration)

"""
database initialization
"""
db.init_app(app)
alembic.init_app(app)

"""
api initialization
"""
CORS(app)
app.register_blueprint(authentication_api, url_prefix='/api/auth')


if __name__ == '__main__':
    app.run(port=6969, debug=True)
