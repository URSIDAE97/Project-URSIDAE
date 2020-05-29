import os


class Configuration:
    """
    configuration constants for URSIDAE server
    """

    """
    database
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/ursidae_server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALEMBIC = {
        'script_location': os.path.join('model', 'migrations')
    }

    """
    security
    """
    JWT_SECRET_KEY = 'BOnQJ7o6SpPsvwlGQ3GuqSB4WK8IblJC'
    JWT_ACCESS_TOKEN_EXPIRES = 900
