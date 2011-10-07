from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Table
from reprap.models.base import Base


TagsIssuesModel = Table('tags_issues', Base.metadata,
                        Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True),
                        Column('issue_id', Integer, ForeignKey('issues.id'), primary_key=True)
)