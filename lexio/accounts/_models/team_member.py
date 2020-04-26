from lexio.base import Base, db


class TeamMember(Base):
    __tablename__ = 'team_members'
    member_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    member = db.relationship("User", backref=db.backref("team_members", cascade="all, delete-orphan"))
    team = db.relationship("Team", backref=db.backref("team_members", cascade="all, delete-orphan"))

    def __init__(self, user_id, team_id):
        self.member_id = user_id
        self.team_id = team_id



