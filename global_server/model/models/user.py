class User:
    """
    data container for UserEntity class
    (prevents mutations of original UserEntity object)
    """

    def __init__(self, user_entity):
        self.id = user_entity.id
        self.username = user_entity.username
        self.password = user_entity.password

    def __str__(self):
        return '<User: { id: %s, username: %s, password: %s }>' \
               % (self.id, self.username, self.password)
