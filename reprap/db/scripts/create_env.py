from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine

def create_schema(engine):
    metadata = MetaData(engine)
    
    users = Table('users', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('username', String(50)),
                  Column('email', String(50))
    )
    
    issues  = Table('issues', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('title', String(50)),
                    Column('description', String(2000)),
                    Column('solved', Integer),
                    Column('created', DateTime),
                    Column('change_time', DateTime),
                    Column('user_id', Integer)
    )
    
    tags  = Table('tags', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String(50))
    )
    
    tags_issues = Table('tags_issues', metadata,
                        Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True),
                        Column('issue_id', Integer, ForeignKey('issues.id'), primary_key=True)
    )

    issue_comments  = Table('issue_comments', metadata,
                            Column('id', Integer, primary_key=True),
                            Column('body', String(300)),
                            Column('created', DateTime),
                            Column('change_time', DateTime),
                            Column('issue_id', Integer),
                            Column('user_id', Integer)
    )        
    
    metadata.create_all()
        
if __name__ == '__main__':
    engine = create_engine('sqlite://', 
                           pool_recycle=3600)
    create_schema(engine)