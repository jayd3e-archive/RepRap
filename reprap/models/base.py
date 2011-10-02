from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

def engine(config):
    create = config.engine + '://'
    #sqlite style configuration
    if config.file:
        create += config.file
    #MySQL style configuration
    elif config.user:
        create += config.user
        if config.pw:
            create += ':' + config.pw
        if config.host:
            create += '@' + config.host
        if config.db:
            create += '/' + config.db

    return create_engine(create, pool_recycle=3600)

def session():
    return sessionmaker()

def base():
    return declarative_base()

Base = base()
Session = session()

def initializeDb(engine):
    Session.configure(bind=engine)
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)
