from reprap.models.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Date, DateTime

class IssueImagesModel(Base):
    __tablename__ = 'issue_images'
    
    id = Column(Integer, primary_key=True)
    directory = Column(String(10))
    filename = Column(String(100))
    filesize = Column(Integer)
    mimetype = Column(String(50))
    issue_id = Column(Integer, ForeignKey('issues.id'))

    def __init__(self, **fields):
        self.__dict__.update(fields)

    def __repr__(self):
        return "<IssueImages('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, 
                                                                      self.directory, 
                                                                      self.filename, 
                                                                      self.filesize, 
                                                                      self.mimetype, 
                                                                      self.issue_id)