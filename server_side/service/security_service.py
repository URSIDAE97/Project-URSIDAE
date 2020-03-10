from .user_service import UserService


class SecurityService:
    """
    services in association with security of the server
    like authorization and authentication of users
    """

    @staticmethod
    def authenticate_user(username, password):
        us = UserService()
        user = us.find_by_username(username)
        if username == user.username and password == user.password:
            return True
        else:
            return False
