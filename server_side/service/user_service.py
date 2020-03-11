from model import db
from model.entities import UserEntity


class UserService:
    """
    services in association with user entity
    """

    @staticmethod
    def find_by_username(username):
        """
        find user in database by username
        :param username: username
        :return: User object or None
        """
        user = db.session.query(UserEntity) \
            .filter(UserEntity.username == username) \
            .first()

        if user:
            return user.data()
        else:
            return None
