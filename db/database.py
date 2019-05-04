from base_engine import Base, engine
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, Boolean, Table
from sqlalchemy.orm import relationship, backref


class CLASS(Base):
    __tablename__ = 'class'

    CLASS_ID = Column(Integer, primary_key=True)
    CLASS = Column(String)


class CLIENTS(Base):
    __tablename__ = 'clients'
    CLIENT_ID = Column(Integer, primary_key=True)
    CLIENT_NAME = Column(String)
    CLIENT_LAST_NAME = Column(String)
    CLIENT_MIDDLE_NAME = Column(String)
    CLIENT_PHONE_NUMBER = Column(String)


class SHOPS(Base):
    __tablename__ = 'shops'

    SHOP_ID = Column(Integer, primary_key=True)
    SHOP_NAME = Column(String)
    SHOP_ADDRESS = Column(String)


class PROVIDER(Base):
    __tablename__ = 'provider'

    PROVIDER_ID = Column(Integer, primary_key=True)
    PROVIDER_ORGANIZATION = Column(String)
    PROVIDER_ADDRESS = Column(String)
    PROVIDER_PHONE_NUMBER = Column(String)


class WORKER_INFO(Base):
    __tablename__ = 'worker_info'

    WORKER_ID = Column(Integer, primary_key=True)
    WORKER_LAST_NAME = Column(String)
    WORKER_NAME = Column(String)
    WORKER_MIDDLE_NAME = Column(String)
    WORKER_PASSPORT_SERIES = Column(String)
    WORKER_PASSPORT_ID = Column(String)
    WORKER_POSITION_HELD = Column(String)
    WORKER_PLACE_OF_RESIDENT = Column(String)


class SALARY(Base):
    __tablename__ = 'salary'
    ID = Column(Integer, primary_key=True)
    WORKER_ID = Column(Integer, ForeignKey('worker_info.WORKER_ID', onupdate="CASCADE", ondelete="CASCADE"))
    WORKER_SALARY = Column(Integer)
    WORKER_PREMIUM = Column(Integer)
    WORKER_PREPAID_EXPENSE = Column(Integer)

    worker_info = relationship("WORKER_INFO",
                               backref=backref("salary", uselist=False),
                               cascade="all, delete-orphan")


class SUPPLY(Base):
    __tablename__ = 'supply'
    ID = Column(Integer, primary_key=True)
    PROVIDER_ID = Column(Integer, ForeignKey('provider.PROVIDER_ID', onupdate="CASCADE", ondelete="CASCADE"))
    SUPPLY_DATE_AND_TIME = Column(TIMESTAMP)
    provider = relationship("PROVIDER",
                            backref="supply", )


association_table = Table('production', Base.metadata,
                          Column('BOOK_IDENTIFIER', Integer,
                                 ForeignKey('book.BOOK_IDENTIFIER', onupdate="CASCADE", ondelete="CASCADE")),
                          Column('ORDER_ID', Integer,
                                 ForeignKey('order_of_books.ORDER_ID', onupdate="CASCADE", ondelete="CASCADE"))
                          )


class BOOK(Base):
    __tablename__ = 'book'
    BOOK_IDENTIFIER = Column(Integer, primary_key=True)
    NAME_OF_BOOK = Column(String)
    AUTHOR_OF_BOOK = Column(String)
    QUANTITY_OF_PAGES = Column(Integer)
    QUANTITY_OF_COPYES = Column(Integer)
    PRICE_OF_BOOK = Column(Integer)

    order_of_books = relationship("ORDER_OF_BOOKS",
                                  secondary=association_table, )


class ORDER_OF_BOOKS(Base):
    __tablename__ = 'order_of_books'
    ORDER_ID = Column(Integer, primary_key=True)
    PROVIDER_ID = Column(Integer, ForeignKey('provider.PROVIDER_ID', onupdate="CASCADE", ondelete="CASCADE"))
    SHOP_ID = Column(Integer, ForeignKey('shops.SHOP_ID', onupdate="CASCADE", ondelete="CASCADE"))
    CLIENT_ID = Column(Integer, ForeignKey('clients.CLIENT_ID', onupdate="CASCADE", ondelete="CASCADE"))
    DATE_OF_ORDER = Column(TIMESTAMP)
    SUMM_OF_PREPAYMENT = Column(Integer)
    DATE_OF_COMPLETION = Column(TIMESTAMP)
    WORKER_ID = Column(Integer, ForeignKey('worker_info.WORKER_ID', onupdate="CASCADE", ondelete="CASCADE"))
    IS_ACTIVE = Column(Boolean)
    CLASS_ID = Column(Integer, ForeignKey('class.CLASS_ID', onupdate="CASCADE", ondelete="CASCADE"))

    book = relationship("BOOK",
                        secondary=association_table, )


if __name__ == '__main__':
    Base.metadata.create_all(engine)
