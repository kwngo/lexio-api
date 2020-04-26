from lexio.base import Base, db


class Team(Base):
    __tablename__ = 'teams'
    name = db.Column(db.String, nullable=False, unique=True, index=True)
    members = db.relationship("User", secondary="team_members")

    def __init__(self, name):
        self.name = name


