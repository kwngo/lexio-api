from lexio.base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref


class TeamMember(Base):
    __tablename__ = 'team_members'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    team_id = Column(Integer, ForeignKey('teams.id'), nullable=False)
    member = relationship("User", backref=backref("team_members", cascade="all, delete-orphan"))
    team = relationship("Team", backref=backref("team_members", cascade="all, delete-orphan"))

    def __init__(self, user_id, team_id):
        self.user_id = user_id
        self.team_id = team_id

