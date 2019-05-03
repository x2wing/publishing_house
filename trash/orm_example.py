# -*- coding: utf-8 -*-


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String
from sqlalchemy import create_engine


Base = declarative_base()

# определяем формат таблицы в БД.
# как бы пост для блога.
class CData(Base):
    __tablename__ = "cdata"

    id = Column(Integer, primary_key=True)
    url = Column(String)
    image = Column(String)
    title = Column(String)
    text = Column(Text)

    def __init__(self, url, image, title, text):
        self.url = url
        self.image = image
        self.title = title
        self.text = text

    def __repr__(self):
        return "CData '%s'" % (self.url)
class Engine:
    def __init__(self):
        self.db_engine = create_engine("sqlite:///data.db", echo=False)
        # создадём таблицы
        Base.metadata.create_all(self.db_engine)