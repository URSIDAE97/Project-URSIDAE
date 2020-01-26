from ..database import database


class Settings(database.Model):

    __tablename__ = 'urs_settings'

    id_setting = database.Column(
        database.Integer,
        primary_key=True,
        autoincrement=True
    )
    setting = database.Column(
        database.String(50),
        nullable=False
    )
    value = database.Column(
        database.String(50),
        nullable=True
    )

    def __init__(self, setting, value):
        self.id_setting = None
        self.setting = setting
        self.value = value

    def __repr__(self):
        print(f'<master_trait({ self.id_setting }, { self.setting }, { self.value })>')
