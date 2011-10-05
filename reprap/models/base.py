from sqlalchemy.ext.declarative import declarative_base

def base():
    return declarative_base()

Base = base()

def initializeBase(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)