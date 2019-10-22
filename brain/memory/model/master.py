from ..hippocampus import database


class Master(database.Model):

    __tablename__ = 'urs_master'

    id_master = database.Column(database.Integer, primary_key=True)
    trait = database.Column(database.String(50))
    value = database.Column(database.String(50))

    def __init__(self):
        self.id_master = None
        self.trait = None
        self.value = None

    @classmethod
    def initialize_master_traits(cls):
        trait = Master()
        database.session.add(trait)
        database.session.commit()
        pass

    def restore_default_master_traits(self):
        pass

    @classmethod
    def get_trait(cls, trait):
        return cls.query.filter_by(trait=trait)
