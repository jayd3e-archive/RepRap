from reprap.models.base import Base
from sqlalchemy import Column, Integer, String, Date, DateTime

class IssueCommentModel(Base):
    __tablename__ = 'issue_comment'
    
    id = Column(Integer, primary_key=True)
    body = Column(String(300))
    issue_id = Column
    user_id = Column(Integer)
    created = Column(DateTime)
    change_time = Column(DateTime)

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Issue('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                                self.body, 
                                                                self.issue_id, 
                                                                self.user_id, 
                                                                self.created, 
                                                                self.change_time)
