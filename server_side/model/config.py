from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic

"""
initialization of database related objects
"""
db = SQLAlchemy()
alembic = Alembic()
