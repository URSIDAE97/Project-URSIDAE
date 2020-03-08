class SecurityService:

    @staticmethod
    def authenticate_user(login, password):
        if login == 'ursidae' and password == 'ursidae':
            return True
        else:
            return False
