from reprap.models.base import Base
from reprap.models.tags import TagsModel
from reprap.models.tags_issues import TagsIssuesModel
from reprap.models.issue_comments import IssueCommentsModel
from reprap.models.issue_images import IssueImagesModel
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.orm import relationship

class IssuesModel(Base):
    __tablename__ = 'issues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    description = Column(String(2000))
    solved = Column(Integer)
    created = Column(DateTime)
    change_time = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))
    tags = relationship(TagsModel,
                        secondary=TagsIssuesModel,
                        backref="issues")
    comments = relationship(IssueCommentsModel,
                            backref="issue")
    images = relationship(IssueImagesModel,
                          backref="issue")

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<Issues('%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                                       self.title, 
                                                                       self.description, 
                                                                       self.solved,
                                                                       self.created, 
                                                                       self.change_time,
                                                                       self.user_id)
