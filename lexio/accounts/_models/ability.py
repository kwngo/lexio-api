from lexio.base import Base
from sqlalchemy import Column, Integer


class Ability(Base):
    __tablename__ = 'abilities'
    name = Column(Integer, primary_key=True)

    def __init__(self, name):
        self.name = name.lower()

    def __repr__(self):
        return '<Ability {}>'

