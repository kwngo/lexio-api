from ._models.user import User
from ._models.team import Team
from ._models.team_member import TeamMember

from pydantic import BaseModel
from sqlalchemy.orm import Session

import bcrypt


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    first_name: str
    last_name: str

def create_user(db : Session, user: UserCreate):
    password_hash = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    user = User(user.email, user.username, password_hash,\
        user.first_name, user.last_name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

class TeamCreate(BaseModel):
    name: str

def create_team(db : Session, team: TeamCreate):
    db_team = Team(name=team.name)
    db.add(db_team)
    db.commit()
    db.refresh(db_team)
    return db_team

def assign_member_to_team(user_id: int, team_id: int, db : Session):
    db_team_member = TeamMember(user_id=user_id, team_id=team_id)
    db.add(db_team_member)
    db.commit()
    db.refresh(db_team_member)
    return db_team_member

