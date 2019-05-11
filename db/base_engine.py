

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config
from db.config import conf

class DB():
    def __init__(self):
        # config = {'db.url': 'postgresql+psycopg2://postgres:1@localhost/publishing_company', 'db.echo': 'True'}
        config = {'db.url': f'{conf.backend}://{conf.user}:{conf.password}@{conf.hostname}:{conf.port}/{conf.database}',
                  'db.echo': 'True'}
        print(config)

        self.engine = engine_from_config(config, prefix='db.')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        self.Base = declarative_base()

    def make_schema(self):
        self.Base.metadata.create_all(self.engine)