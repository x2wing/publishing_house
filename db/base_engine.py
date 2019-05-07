

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config


class DB():
    def __init__(self):
        # config = {'db.url': 'postgresql+psycopg2://postgres:1@localhost/publishing_company', 'db.echo': 'True'}
        config = {'db.url': 'postgresql+psycopg2://postgres:123@localhost/publishing_company', 'db.echo': 'True'}

        self.engine = engine_from_config(config, prefix='db.')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.Base = declarative_base()

    def make_schema(self):
        self.Base.metadata.create_all(self.engine)