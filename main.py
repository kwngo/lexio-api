from lexio.accounts import create_team, create_user, assign_member_to_team
from lexio.accounts.models import User
from .db import SessionLocal, engine

from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.exc import SQLAlchemyError

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class Registration(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    password_confirmation: str
    team_name: str


@app.get("/register")
def register(registration: Registration, db: Session = Depends(get_db)):
    registration_dict = registration.dict()
    email = registration_dict.get('email')
    username = registration_dict.get('username')
    first_name = registration_dict.get('first_name')
    last_name = registration_dict.get('last_name')
    password = registration_dict.get('password')
    password_confirmation = registration_dict.get('password_confirmation')
    team_name = registration_dict.get('team_name')

    user_exists = db.session.query(User) \
        .filter((User.email == email) | (User.username == username)) \
        .count() > 0

    if user_exists:
        raise HTTPException(status_code=400, detail="User could not be created.")

    if password != password_confirmation:
        raise HTTPException(status_code=400, detail="Passwords do not match.")

    try:
        team = create_team(db=db, team={"name": team_name})
        user = create_user(db=db, user={"email": email, "password": password, "username": username, "first_name": first_name, "last_name": last_name})
        assign_member_to_team(user_id=user.id, team_id=team.id)
    except SQLAlchemyError:
        raise HTTPException(status_code=400, detail="New account creation failed")

    return registration

