from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate


db = SQLAlchemy()


def initialize_memory(app):
    """ initialize database connection for the server
    """

    app.config['SQLALCHEMY_DATABASE_URI'] = Config.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate = Migrate(app, db)
