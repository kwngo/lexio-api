from sqlalchemy import Column, String, Integer, DateTime, MetaData, func, ForeignKey
from sqlalchemy.orm import relationship

from lexio.base import Base



class User(Base):
    __tablename__ = 'users'
    username = Column(String, nullable=False, unique=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password_hash = Column(String(), nullable=False)
    confirmation_token = Column(String)
    confirmed_at = Column(DateTime)
    confirmation_sent_at = Column(DateTime)
    reset_password_token = Column(String)
    reset_password_sent_at = Column(DateTime)
    roles = relationship('Role', secondary='user_roles')
    teams = relationship('Team', secondary='team_members')
    articles = relationship('Article')

    def __init__(self, email, password_hash, account_id, roles=None, teams=None, confirmation_token=None, confirmed_at=None, confirmation_sent_at=None, reset_password_token=None, reset_password_sent_at=None):
        self.email = email
        self.password_hash = password_hash
        self.account_id = account_id
        self.confirmation_token = confirmation_token
        self.confirmed_at = confirmed_at
        self.confirmation_sent_at = confirmation_sent_at
        self.reset_password_token = reset_password_token
        self.reset_password_sent_at = reset_password_sent_at

    def add_roles(self, *roles):
        self.roles.extend([role for role in roles if role not in self.roles])

    def remove_roles(self, *roles):
        self.roles = [role for role in self.roles if role not in roles]

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    @property
    def get_id(self):
        return str(self.email)



