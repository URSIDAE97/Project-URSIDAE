from model import db
from .mixin import Mixin
from ..models import User


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

    def get_data(self):
        return User(self)

    def __str__(self):
        return User(self).__str__()
