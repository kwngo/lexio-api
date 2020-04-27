from db import DeclarativeBase
from sqlalchemy import Column, Integer, DateTime, MetaData, func


class Base(DeclarativeBase):
    __abstract__  = True
    id            = Column(Integer, primary_key=True)
    date_created  = Column(DateTime,  default=func.current_timestamp())
    date_modified = Column(DateTime,  default=func.current_timestamp(),
                                           onupdate=func.current_timestamp())
    metadata = MetaData()

    def __repr__(self):
        return f'<{self.__class__.__name__}(id="{self.id}")>'

    def __str__(self):
        return f'{self.__class__.__name__}(id="{self.id}")'

