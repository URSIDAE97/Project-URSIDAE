import sqlite3


def sql_test():
    connection = sqlite3.connect('memory.db')
    cursor = connection.cursor()

    create_table = 'CREATE TABLE test (column1 text, column2 text)'

    cursor.execute(create_table)
