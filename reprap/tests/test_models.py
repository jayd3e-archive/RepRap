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
        
        user = UsersModel(username="jayd3e",
                          email="test@gmail.com")
        session.add(user)
        user.issues.append(issue)
        
        tag = TagsModel(name="python")
        issue.tags.append(tag)
        
        comment = IssueCommentsModel(body="U SUCK",
                                     created=datetime.now(),
                                     change_time=datetime.now())
        issue.comments.append(comment)
         
        session.flush()
        self.assertTrue(str(issue).startswith('<Issues'),
                        msg="str(IssuesModel) must start with '<Issues'")
        self.assertIn(issue, user.issues)
        self.assertEqual(issue.user, user)
        self.assertIn(tag, issue.tags)
        self.assertIn(issue, tag.issues)
        self.assertIn(comment, issue.comments)
        self.assertEqual(comment.issue, issue)
        
    def testIssueCommentsModel(self):
        comment = IssueCommentsModel(body="U SUCK",
                                     created=datetime.now(),
                                     change_time=datetime.now())
        
        session = self.Session()
        session.add(comment)
        
        user = UsersModel(username="jayd3e",
                          email="test@gmail.com")
        session.add(user)
        user.comments.append(comment)
        
        issue = IssuesModel(title="Important Issue",
                            description="This issue is really important.",
                            solved=0,
                            created=datetime.now(),
                            edited=datetime.now())
        session.add(issue)
        issue.comments.append(comment)
        
        session.flush()
        self.assertTrue(str(comment).startswith('<IssueComments'),
                        msg="str(IssueCommentsModel) must start with '<IssueComments'")
        self.assertIn(comment, user.comments)
        self.assertEqual(comment.user, user)
        self.assertIn(comment, issue.comments)
        self.assertEqual(comment.issue, issue)