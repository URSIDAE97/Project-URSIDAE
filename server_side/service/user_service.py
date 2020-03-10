from model import db
from model.entities import UserEntity


class UserService:
    """
    services in association with user entity
    """

    @staticmethod
    def find_by_username(username):
        user = db.session.query(UserEntity) \
            .filter(UserEntity.username == username) \
            .first()

        return user.data()
