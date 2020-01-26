from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def initialize_memory(app):
    """ initialize memory of the application by connecting to database
    """

    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
