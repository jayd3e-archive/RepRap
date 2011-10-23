from reprap.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.associationproxy import association_proxy

class IssueCommentsModel(Base):
    __tablename__ = 'issue_comments'
    
    id = Column(Integer, primary_key=True)
    body = Column(String(300))
    created = Column(DateTime)
    change_time = Column(DateTime)
    score = Column(Integer(100), default=0)
    issue_id = Column(Integer, ForeignKey('issues.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    voted_users = association_proxy('users_comments', 'user')

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<IssueComments('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                                        self.body, 
                                                                        self.issue, 
                                                                        self.user, 
                                                                        self.created, 
                                                                        self.change_time)
