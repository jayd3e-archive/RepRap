from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import MetaData
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from reprap.db.config import DbConfig
from reprap.db.config import TestConfig

class CreateEnv(object):
    def __init__(self):
        pass

    def create_db(self, config):
        create = config.engine + '://'

        if config.user:
            create += config.user
        elif config.file:
            create += config.file

        if config.pw:
            create += ':' + config.pw
        if config.host:
            create += '@' + config.host
        if config.db:
            create += '/' + config.db

        self.db = create_engine(create, pool_recycle=3600)

    def create_schema(self):
        metadata = MetaData(self.db)

if __name__ == '__main__':
    c = CreateEnv()
    c.create_db(DbConfig)
    c.create_schema()
