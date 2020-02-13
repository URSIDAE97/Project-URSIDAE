from ..database import database


class Master(database.Model):

    __tablename__ = 'urs_master'

    id_master = database.Column(
        database.Integer,
        primary_key=True,
        autoincrement=True
    )
    trait = database.Column(
        database.String(50),
        nullable=False
    )
    value = database.Column(
        database.String(50),
        nullable=True
    )

    def __init__(self, trait, value):
        self.id_master = None
        self.trait = trait
        self.value = value

    def __repr__(self):
        print(f'<master_trait({ self.id_master }, { self.trait }, { self.value })>')

    @staticmethod
    def initialize_master_traits():
        global initial_traits
        database.session.bulk_save_objects(initial_traits)
        database.session.commit()

    @staticmethod
    def restore_default_master_traits():
        # TODO: restoring traits have to work differently
        global default_traits
        database.session.add(default_traits)
        database.session.commit()

    @classmethod
    def get_trait(cls, trait):
        return cls.query.filter_by(trait=trait)

    @classmethod
    def set_trait(cls, trait, value):
        trait = cls.get_trait(trait)
        if trait:
            trait.value = value
        database.session.add(trait)
        database.session.commit()


initial_traits = [
    Master('name', ''),
    Master('password', '')
]

default_traits = [

]
