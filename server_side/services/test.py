from data import db, Result
from flask import jsonify


class TestService:

    @staticmethod
    def db_test():
        result = Result('just a test', 'asdasdasd', 'asdasdsdasd')
        print(result)
        db.session.add(result)
        db.session.commit()

        return 'succes'
