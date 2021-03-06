from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, Boolean, Table
from sqlalchemy.orm import relationship, backref

from db.base_engine import DB

db = DB()


class CLASS(db.Base):
    __tablename__ = 'class'

    class_id = Column(Integer, primary_key=True)
    class_name = Column(String)


class CLIENTS(db.Base):
    __tablename__ = 'clients'

    client_id = Column(Integer, primary_key=True)
    client_name = Column(String)
    client_last_name = Column(String)
    client_middle_name = Column(String)
    client_phone_number = Column(String)


class SHOPS(db.Base):
    __tablename__ = 'shops'

    shop_id = Column(Integer, primary_key=True)
    shop_name = Column(String)
    shop_address = Column(String)


class PROVIDER(db.Base):
    __tablename__ = 'provider'

    provider_id = Column(Integer, primary_key=True)
    provider_organization = Column(String)
    provider_address = Column(String)
    provider_phone_number = Column(String)


class WORKER_INFO(db.Base):
    __tablename__ = 'worker_info'

    worker_id = Column(Integer, primary_key=True)
    worker_last_name = Column(String)
    worker_name = Column(String)
    worker_middle_name = Column(String)
    worker_passport_series = Column(String)
    worker_passport_id = Column(String)
    worker_position_held = Column(String)
    worker_place_of_resident = Column(String)


class SALARY(db.Base):
    __tablename__ = 'salary'

    id_ = Column(Integer, primary_key=True)
    worker_id = Column(Integer, ForeignKey('worker_info.worker_id', onupdate="CASCADE", ondelete="CASCADE"))
    worker_salary = Column(Integer)
    worker_premium = Column(Integer)
    worker_prepaid_expense = Column(Integer)

    worker_info = relationship("WORKER_INFO",
                               backref=backref("salary", uselist=False), )


class SUPPLY(db.Base):
    __tablename__ = 'supply'

    id_ = Column(Integer, primary_key=True)
    provider_id = Column(Integer, ForeignKey('provider.provider_id', onupdate="CASCADE", ondelete="CASCADE"))
    supply_date_and_time = Column(TIMESTAMP)
    provider = relationship("PROVIDER",
                            backref="supply", )


PRODUCTION = Table(
    'production', db.Base.metadata,
    Column('book_identifier', Integer,
           ForeignKey('book.book_identifier', onupdate="CASCADE", ondelete="CASCADE")),
    Column('order_id', Integer,
           ForeignKey('order_of_books.order_id', onupdate="CASCADE", ondelete="CASCADE")),
)


class BOOK(db.Base):
    __tablename__ = 'book'

    book_identifier = Column(Integer, primary_key=True)
    name_of_book = Column(String)
    author_of_book = Column(String)
    quantity_of_pages = Column(Integer)
    quantity_of_copyes = Column(Integer)
    price_of_book = Column(Integer)

    order_of_books = relationship("ORDER_OF_BOOKS",
                                  secondary=PRODUCTION, )

    def __init__(self, name_of_book, author_of_book, quantity_of_pages, quantity_of_copyes, price_of_book):
        self.name_of_book = name_of_book
        self.author_of_book = author_of_book
        self.quantity_of_pages = quantity_of_pages
        self.quantity_of_copyes = quantity_of_copyes
        self.price_of_book = price_of_book


class ORDER_OF_BOOKS(db.Base):
    __tablename__ = 'order_of_books'

    order_id = Column(Integer, primary_key=True)
    order_name = Column(String)
    provider_id = Column(Integer, ForeignKey('provider.provider_id', onupdate="CASCADE", ondelete="CASCADE"))
    shop_id = Column(Integer, ForeignKey('shops.shop_id', onupdate="CASCADE", ondelete="CASCADE"))
    client_id = Column(Integer, ForeignKey('clients.client_id', onupdate="CASCADE", ondelete="CASCADE"))
    date_of_order = Column(TIMESTAMP)
    summ_of_prepayment = Column(Integer)
    date_of_completion = Column(TIMESTAMP)
    worker_id = Column(Integer, ForeignKey('worker_info.worker_id', onupdate="CASCADE", ondelete="CASCADE"))
    is_active = Column(Boolean)
    class_id = Column(Integer, ForeignKey('class.class_id', onupdate="CASCADE", ondelete="CASCADE"))

    book = relationship("BOOK",
                        secondary=PRODUCTION, )


if __name__ == '__main__':
    # def csv_dict_reader(file_obj):
    #     """
    #     Read a CSV file using csv.DictReader
    #     """
    #     reader = csv.DictReader(file_obj, delimiter=';')
    #     for line in reader:
    #         new_element = BOOK(line['Авторы'], line['Название'], randint(180, 379), randint(1, 3), randint(340, 5000))
    #         db.session.add(new_element)
    #
    #     db.session.commit()
    #
    #
    # with open("data.csv") as f_obj:
    #     csv_dict_reader(f_obj)
    #
    # # for i in db.session.query(CLASS.class_name):
    # #     print(i[0])
    # #     # print({i.class_id:i.class_name})

    db.make_schema()
