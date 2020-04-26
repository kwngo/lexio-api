from lexio.base import Base, db
from .ability import Ability


class Role(Base):
    __tablename__ = 'roles'
    name = db.Column(db.String(), unique=True)
    abilities = db.relationship('Ability', secondary='abilities', backref='roles')

    def __init__(self, name):
        self.name = name.lower()

    def add_abilities(self, *abilities):
        for ability in abilities:
            existing_ability = Ability.query.filter_by(
                    name=ability
                    ).first()
            if not existing_ability:
                existing_ability = Ability(ability)
                db.session.add(existing_ability)
                db.session.commit()
            self.abilities.append(existing_ability)

    def remove_abilities(self, *abilities):
        for ability in abilities:
            existing_ability = Ability.query.filter_by(name=ability).first()
            if existing_ability and existing_ability in self.abilities:
                self.abilities.remove(existing_ability)


