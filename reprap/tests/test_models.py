import unittest
from datetime import datetime
from reprap.models.issues import IssuesModel
from reprap.models.issue_comments import IssueCommentsModel
from reprap.models.tags import TagsModel
from reprap.models.tags_issues import TagsIssuesModel
from reprap.models.users import UsersModel
from reprap.models.base import initializeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config

class TestModels(unittest.TestCase):
    def setUp(self):
        settings = {'sqlalchemy.url' : 'sqlite://'}
        
        engine = engine_from_config(settings, 'sqlalchemy.')
        initializeBase(engine)
        self.Session = sessionmaker(bind=engine)
    
    def testIssuesModel(self):
        issue = IssuesModel(title="Important Issue",
                            description="This issue is really important.",
                            solved=0,
                            created=datetime.now(),
                            edited=datetime.now())
        
        session = self.Session()
        session.add(issue)

        session.flush()
        session.query(IssuesModel).delete()
        self.assertTrue(str(issue).startswith('<Issues'),
                        msg="str(IssuesModel) must start with '<Issues'")