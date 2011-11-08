from reprap.models.base import Base
from reprap.models.users import UsersModel
from reprap.models.issue_comments import IssueCommentsModel
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class UsersCommentsModel(Base):
    __tablename__ = 'users_comments'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('issue_comments.id'))
    vote = Column(Integer(1))
    
    user = relationship(UsersModel,
                        backref="users_comments")
    comment = relationship(IssueCommentsModel,
                           backref="users_comments")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<UsersComments('%s', '%s', '%s')>" % (self.user_id,
                                                      self.comment_id,
                                                      self.vote)    