from lexio.base import Base, db


class Ability(Base):
    __tablename__ = 'abilities'
    name = db.Column(db.Integer, primary_key=True)

    def __init__(self, name):
        self.name = name.lower()

    def __repr__(self):
        return '<Ability {}>'

