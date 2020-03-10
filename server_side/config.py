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
