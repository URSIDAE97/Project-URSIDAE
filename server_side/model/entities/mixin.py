from model import db
from datetime import datetime


class Mixin(object):
    """
    mixin columns added to every table
    """

    # unique identifier
    id = db.Column(
        db.Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )
    # creation date and time
    created = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    # last edition date and time
    updated = db.Column(
        db.DateTime,
        onupdate=datetime.utcnow
    )
