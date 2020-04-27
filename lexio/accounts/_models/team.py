from lexio.base import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship


class Team(Base):
    __tablename__ = 'teams'
    name = Column(String, nullable=False, unique=True, index=True)
    members = relationship("User", secondary="team_members")

    def __init__(self, name):
        self.name = name


