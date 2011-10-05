from reprap.models.base import Base
from sqlalchemy import Column, Integer, String, Date, DateTime

class IssueModel(Base):
    __tablename__ = 'issues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(2000))
    solved = Column(Integer)
    user_id = Column(Integer)
    created = Column(DateTime)
    change_time = Column(DateTime)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Issue('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                                      self.title, 
                                                                      self.description, 
                                                                      self.solved,
                                                                      self.user_id,
                                                                      self.created, 
                                                                      self.change_time)
