

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import engine_from_config

# config = {'db.url': 'postgresql+psycopg2://postgres:1@localhost/publishing_company', 'db.echo': 'True'}
config = {'db.url': 'postgresql+psycopg2://postgres:1@localhost/publishing_company2', 'db.echo': 'True'}

engine = engine_from_config(config, prefix='db.')
Session = sessionmaker(bind=engine)

Base = declarative_base()