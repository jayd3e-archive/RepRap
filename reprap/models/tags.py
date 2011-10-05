from reprap.models.base import Base
from sqlalchemy import Column, Integer, String, Date, DateTime

class TagsModel(Base):
    __tablename__ = 'tags'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Issue('%s', '%s')>" % (self.id, 
                                        self.name)