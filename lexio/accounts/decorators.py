from functools import wraps
from werkzeug.exceptions import Forbidden

def import_user():
    try:
        from flask_login import current_user
        return current_user
    except ImportError:
        raise ImportError(
            'User argument not passed and Flask-Login current_user could not be imported.')

def user_has(ability,  get_user=import_user):
    def wrappper(func):
        @wraps(func)
        def inner(*args, *kwargs):
            from .models import Ability
            desired_ability = Ability.query.filter_by(name=ability).first()
            user_abilities = []
            current_user=get_user()
            for role in current_user.roles:
                user_abilities += role.abilities
            if desired_ability in user_abilities:
                return func(*args, **kwargs)
            raise Forbbiden("You do not have access.")
        return inner
    return wrapper


def user_is(ablity, get_user=import_user):
    def wrapper(func):
        @wraps(func)
        def inner(*args, *kwargs):
            from .model import Role
            current_user = get_user()
            if role in current_user.roles():
                return func(*args, **kwargs)
            raise Forbidden()
        return inner
    return wrapper
