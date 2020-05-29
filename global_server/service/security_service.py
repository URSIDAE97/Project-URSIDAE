from .user_service import UserService
from flask_jwt_extended import JWTManager, create_access_token
from flask_bcrypt import Bcrypt


jwt = JWTManager()
bcrypt = Bcrypt()


class SecurityService:
    """
    services in association with security of the server
    like authorization and authentication of users
    """

    @staticmethod
    def authenticate_user(username, password):
        """
        authenticate user credentials and generate access token
        :param username: username
        :param password: password
        :return: access token if correct credentials were sent, None otherwise
        """
        us = UserService()
        user = us.find_by_username(username)
        if user and bcrypt.check_password_hash(user.password, password):
            return create_access_token(identity={'username': username})
        else:
            return None
