from db.database import CLASS, BOOK, CLIENTS, SHOPS, PROVIDER, WORKER_INFO, SALARY, ORDER_OF_BOOKS, SUPPLY, db
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, Boolean, Table
from sqlalchemy.orm import relationship, backref
import sqlalchemy as sa
import pandas as pd
import os
import subprocess
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Reports():
    def __init__(self, file_name, sa_query, columns_list):
        self.report_name = file_name     # r'Отчет Заказы по менеджерам.xlsx'
        self.request = sa_query          # sqlalchemy запрос
        self.columns_list = columns_list # ['Фамилия', 'Имя', 'Отчество', 'Название заказа', 'Дата заказа', 'Дата окончания заказа'])
        self.create()
        self.open()




    def create(self):
        df = pd.read_sql_query(self.request.statement, db.engine)
        print(df)
        df.to_excel(self.report_name,
                    header=self.columns_list)

    def open(self):
        os.system(f'start "" "{self.report_name}"')


class Order_to_worker(Reports):
    def __init__(self):
        request = db.session.query(WORKER_INFO.worker_last_name,
                                   WORKER_INFO.worker_name,
                                   WORKER_INFO.worker_middle_name,
                                   ORDER_OF_BOOKS.order_name,
                                   ORDER_OF_BOOKS.date_of_completion,
                                   ORDER_OF_BOOKS.date_of_order). \
                                join(ORDER_OF_BOOKS)
        header = ['Фамилия', 'Имя', 'Отчество', 'Название заказа', 'Дата заказа', 'Дата окончания заказа']
        super().__init__(r'Отчет Заказы по менеджерам.xlsx', request, header)




class Client_and_class(Reports):
    def __init__(self):
        request = db.session.query(CLASS.class_name,
                                   CLIENTS.client_last_name,
                                   CLIENTS.client_name,
                                   CLIENTS.client_middle_name, ). \
                                join(ORDER_OF_BOOKS). \
                                join(CLIENTS)
        header = ['Класс обслуживания', 'Фамилия', 'Имя', 'Отчество']
        super().__init__(r'Отчет Классы обслуживания клиентов.xlsx', request, header)


if __name__ == '__main__':
    Order_to_worker()
    Client_and_class()