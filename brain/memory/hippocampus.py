import sqlite3

from .database import database
from .model import *


# -- initialize memory of the application by connecting to database -- #
def initialize_memory(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////memory/memory.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)


# -- initialize default settings and parameters on registering new master -- #
def initialize_settings_and_properties():
    create_tables()
    Master.initialize_master_traits()


# -- creates tables in database -- #
def create_tables():
    connection = sqlite3.connect('./memory/memory.db')
    cursor = connection.cursor()

    create_query = 'CREATE TABLE urs_master (' \
                   'id_master INTEGER, ' \
                   'trait text,' \
                   'value text)'
    cursor.execute(create_query)

    create_query = 'CREATE TABLE urs_settings (' \
                   'id_setting INTEGER, ' \
                   'setting text,' \
                   'value text)'
    cursor.execute(create_query)

    connection.close()
