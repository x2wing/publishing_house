import os

import pandas as pd

from db.database import CLASS, CLIENTS, WORKER_INFO, ORDER_OF_BOOKS, db


class Reports():
    def __init__(self, name, sa_query, columns_list):
        self.__name = name
        self.report_name = f'{name}.xlsx'  # r'Отчет Заказы по менеджерам.xlsx'
        self.request = sa_query  # sqlalchemy запрос
        self.columns_list = columns_list  # ['Фамилия', 'Имя', 'Отчество', 'Название заказа', 'Дата заказа', 'Дата окончания заказа'])
        self.create()
        self.open()

    @property
    def name(self):
        return self.__name

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
        super().__init__(r'Отчет Заказы по менеджерам', request, header)


class Client_and_class(Reports):
    def __init__(self):
        request = db.session.query(CLASS.class_name,
                                   CLIENTS.client_last_name,
                                   CLIENTS.client_name,
                                   CLIENTS.client_middle_name, ). \
            join(ORDER_OF_BOOKS). \
            join(CLIENTS)
        header = ['Класс обслуживания', 'Фамилия', 'Имя', 'Отчество']
        super().__init__(r'Отчет Классы обслуживания клиентов', request, header)


if __name__ == '__main__':
    Order_to_worker()
    Client_and_class()
