from lexio.base import Base
from sqlalchemy import Column, Integer, ForeignKey


class UserRole(Base):
    __tablename__ = 'user_roles'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'), nullable=False)

    def __init__(self, user_id, role_id):
        self.user_id = user_id
        self.role_id = role_id


