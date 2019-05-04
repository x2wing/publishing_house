import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, Table, TIMESTAMP, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = sqlalchemy.create_engine("postgresql+psycopg2://postgres:1@localhost/test", echo=True)
Base = declarative_base()
session = sessionmaker(bind=engine)()

# class User(base):
#     __tablename__ = "users"
#     uid = Column(Integer, primary_key=True)
#     username = Column(String)
#
#
#
#     cars = relationship("Car", secondary=association_table, back_populates="owners")
#
#
# class Car(base):
#     __tablename__ = "cars"
#     cid = Column(Integer, primary_key=True)
#     model = Column(String)
#
#
#
#     owners = relationship("User", secondary=association_table, back_populates="cars")
#
#
# association_table = Table("owners_to_cars", base.metadata,
#
#                           Column("owner_id", Integer, ForeignKey("users.uid")),
#                           Column("car_id", Integer, ForeignKey("cars.cid")))

association_table = Table('production', Base.metadata,
                          Column('BOOK_IDENTIFIER', Integer, ForeignKey('book.BOOK_IDENTIFIER')),
                          Column('ORDER_ID', Integer, ForeignKey('order_of_books.ORDER_ID'))
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
                                  secondary=association_table)


class ORDER_OF_BOOKS(Base):
    __tablename__ = 'order_of_books'
    ORDER_ID = Column(Integer, primary_key=True)
    DATE_OF_ORDER = Column(TIMESTAMP)
    SUMM_OF_PREPAYMENT = Column(Integer)
    DATE_OF_COMPLETION = Column(TIMESTAMP)
    IS_ACTIVE = Column(Boolean)


Base.metadata.create_all(engine)

# user_a = User(username="Andrew")
# session.add(user_a)
# car_a = Car(model="Accord")
# user_a.cars.append(car_a)
#
# car_b = Car(model="BMW")
# user_a.cars.append(car_b)
#
# user_b = User(username="Beverly")
# user_b.cars.append(car_b)
