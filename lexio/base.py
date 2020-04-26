from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    __abstract__  = True
    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<{self.__class__.__name__}(id="{self.id}")>'

    def __str__(self):
        return f'{self.__class__.__name__}(id="{self.id}")'

