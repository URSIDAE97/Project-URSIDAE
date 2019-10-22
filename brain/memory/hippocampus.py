from flask_sqlalchemy import SQLAlchemy

connection = None   # for creating connection to database
cursor = None       # for reading / writing data to database

database = SQLAlchemy()


def initialize_memory(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    database.init_app(app)


# def sql_test():
#     global connection
#     global cursor
#     connection = sqlite3.connect('./memory/memory.db')
#     cursor = connection.cursor()
#
#
# def create_table():
#     global cursor
#     create = 'CREATE TABLE test (column_one text, column_two text)'
#     cursor.execute(create)
#
#
# def add_data():
#     global cursor
#     test = ('aaa', 'bbb')
#     insert_query = 'INSERT INTO test VALUES (?, ?)'
#     cursor.execute(insert_query, test)
#     connection.com
