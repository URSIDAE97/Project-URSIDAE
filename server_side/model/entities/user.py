from model import db
from .mixin import Mixin


class UserEntity(Mixin, db.Model):
    """
    user entity to store information in the database
    """
    __tablename__ = 'urs_user'

    # unique username
    username = db.Column(
        db.Unicode(),
        unique=True,
        nullable=False,
        index=True
    )
    # password encrypted with hashing
    password = db.Column(
        db.Unicode(),
        unique=False,
        nullable=False
    )

    def data(self):
        return User(self)

    def __str__(self):
        return User(self).__str__()


class User:
    """
    additional class serving only as a data container
    to prevent mutations of original user object
    """

    def __init__(self, user_entity):
        self.id = user_entity.id
        self.username = user_entity.username
        self.password = user_entity.password

    def __str__(self):
        return '<User: { id: %s, username: %s, password: %s }>' \
               % (self.id, self.username, self.password)
