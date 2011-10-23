import unittest
import os
import base64
from datetime import datetime
from reprap.models.issues import IssuesModel
from reprap.models.issue_comments import IssueCommentsModel
from reprap.models.issue_images import IssueImagesModel
from reprap.models.tags import TagsModel
from reprap.models.tags_issues import TagsIssuesModel
from reprap.models.users_comments import UsersCommentsModel
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
        
    def testTagsModel(self):
        tag = TagsModel(name="python")
        
        session = self.Session()
        session.add(tag)
        
        issue = IssuesModel(title="Important Issue",
                            description="This issue is really important.",
                            solved=0,
                            created=datetime.now(),
                            edited=datetime.now())
        tag.issues.append(issue)
        
        session.flush()
        self.assertTrue(str(tag).startswith('<Tags'),
                        msg="str(TagsModel) must start with '<Tags'")
        self.assertIn(issue, tag.issues)
        self.assertIn(tag, issue.tags)
        
    def testUsersModel(self):
        user = UsersModel(username="jayd3e",
                          email="test@gmail.com")
        
        session = self.Session()
        session.add(user)
        
        issue = IssuesModel(title="Important Issue",
                            description="This issue is really important.",
                            solved=0,
                            created=datetime.now(),
                            edited=datetime.now())
        user.issues.append(issue)
        
        comment = IssueCommentsModel(body="U SUCK",
                                     created=datetime.now(),
                                     change_time=datetime.now())
        user.comments.append(comment)
        
        session.flush()
        self.assertTrue(str(user).startswith('<Users'),
                        msg="str(UsersModel) must start with '<Users'")
        self.assertIn(comment, user.comments)
        self.assertEqual(comment.user, user)
        self.assertIn(issue, user.issues)
        self.assertEqual(issue.user, user)
        
    def testIssueImagesModel(self):
        uid = os.urandom(10)
        hex_uid = base64.b64encode(uid)
        image = IssueImagesModel(directory = hex_uid.upper(),
                                 filename = 'Butterflies.jpg',
                                 filesize = 101010101,
                                 mimetype = 'image/jpeg')
        
        session = self.Session()
        session.add(image)
        
        issue = IssuesModel(title="Important Issue",
                            description="This issue is really important.",
                            solved=0,
                            created=datetime.now(),
                            edited=datetime.now())
        image.issue = issue
        
        session.flush()
        self.assertTrue(str(image).startswith('<IssueImages'),
                        msg="str(IssueImagesModel) must start with '<IssueImages'")
        self.assertIn(image, issue.images)
        self.assertEqual(image.issue, issue)
        
    def testUsersCommentsModel(self):
        user = UsersModel(id=5246,
                          username="jayd3e",
                          email="test@gmail.com")
                
        comment = IssueCommentsModel(id=5678,
                                     body="U SUCK",
                                     created=datetime.now(),
                                     change_time=datetime.now())
        
        voted_comment = UsersCommentsModel(user_id=5246,
                                           comment_id=5678,
                                           vote=1)
        session = self.Session()
        session.add(user)
        session.add(comment)
        session.add(voted_comment)
        
        session.flush()
        self.assertTrue(str(voted_comment).startswith('<UsersComments'),
                        msg="str(UsersCommentsModel) must start with '<UsersComments'")
        self.assertIn(comment, user.voted_comments)
        self.assertEqual(user, voted_comment.user)
        self.assertEqual(user.users_comments, [voted_comment])
        self.assertIn(user, comment.voted_users)
        self.assertEqual(comment, voted_comment.comment)
        self.assertEqual(comment.users_comments, [voted_comment])