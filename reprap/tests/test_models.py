import unittest
from reprap.models.base import initializeBase
from sqlalchemy.org import sessionmaker
from sqlalchemy import engine_from_config

class TestModels(unittest.TestCase):
    def setUp(self):
        settings['sqlalchemy.url'] = 'sqlite://'
        
        engine = engine_from_config(settings, 'sqlalchemy.')
        initializeBase(engine)
        self.Session = sessionmaker(bind=engine)
    
    def testIssuesModel(self):
        session = self.Session()