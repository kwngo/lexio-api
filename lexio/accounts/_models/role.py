from lexio.base import Base
from .ability import Ability
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Role(Base):
    __tablename__ = 'roles'
    name = Column(String(), unique=True)
    abilities = relationship('Ability', secondary='abilities', backref='roles')

    def __init__(self, name):
        self.name = name.lower()

    # def add_abilities(self, *abilities):
    #     for ability in abilities:
    #         existing_ability = Ability.query.filter_by(
    #                 name=ability
    #                 ).first()
    #         if not existing_ability:
    #             existing_ability = Ability(ability)
    #             session.add(existing_ability)
    #             session.commit()
    #         self.abilities.append(existing_ability)
    #
    # def remove_abilities(self, *abilities):
    #     for ability in abilities:
    #         existing_ability = Ability.query.filter_by(name=ability).first()
    #         if existing_ability and existing_ability in self.abilities:
    #             self.abilities.remove(existing_ability)
    #
    #
