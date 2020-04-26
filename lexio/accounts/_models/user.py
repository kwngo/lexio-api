from lexio.base import Base, db


class User(Base):
    __tablename__ = 'users'
    email = db.Column(db.String, nullable=False, unique=True, index=True)
    password_hash = db.Column(db.String(), nullable=False)
    confirmation_token = db.Column(db.String)
    confirmed_at = db.Column(db.DateTime)
    confirmation_sent_at = db.Column(db.DateTime)
    reset_password_token = db.Column(db.String)
    reset_password_sent_at = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary='user_roles')
    teams = db.relationship('Team', secondary='team_members')
    articles = db.relationship('Article')

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



