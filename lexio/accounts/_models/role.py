from lexio.base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'roles'
    name = Column(String(), unique=True)

    def __init__(self, name):
        self.name = name.lower()
