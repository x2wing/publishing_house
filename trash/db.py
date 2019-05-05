import psycopg2
from psycopg2.extensions import AsIs
import io
import hashlib
import os
import numpy as np
import tempfile
import h5py
import pickle
from tzlocal import get_localzone

get_localzone()


conn_params = dict(
            database='publishing_company',
            user='postgres',
            password='1',
            host='localhost',
            port=5432
        )




class DBConnection:
    """
    Класс низкоуровневого обращения к БД
    сначала выполняем метод execute_sql - запуск команды sql
    execute_sql получает число записей ответа в self._rowcount
    затем, если нужно, получаем результать методом get_result
    """

    def __init__(self, connection_params):
        self.conn = psycopg2.connect(**connection_params)
        self._rowcount = None

    @property
    def rowcount(self):
        """Получение числа записей ответа от БД"""
        return self._rowcount

    def execute_sql(self, sql_command, params):
        """ Выполнение sql команды (результат возвращается get_result, если необходимо)"""
        try:
            self.cur = self.conn.cursor()
            self.cur.execute(sql_command, params)
            self._rowcount = self.cur.rowcount
            self.conn.commit()
        except Exception as err:
            print(f'{err}')
            self.conn.rollback()

    def get_result(self):
        """
        Получить ответ от сервера
        :return: итератор по строкам ответа из БД
        """
        try:
            yield from self.cur.fetchall()
        except psycopg2.ProgrammingError as err:
            print(f'Connection error {err.pgerror}')

    def __del__(self):
        """деструктор. Закрывает курсор и подключение при уничтожении объекта"""
        try:
            self.cur.close()
        except Exception as err:
            print(err)
        self.conn.close()


class DB:
    """ api обращения к БД"""

    def __init__(self, con_params):
        """
        Инициализация подключения. Получение списка всех моделей
        :param con_params: словарь параметров подключения
        """
        self.db = DBConnection(con_params)

    @staticmethod
    def test_connection(conn_params):
        """
        Проверка на возможность соединения с базой
        """

        try:
            # Если атрибут соединения closed == 0 - соединение устанавливается
            db_test = DBConnection(conn_params)
            if not db_test.conn.closed:
                return True
        except psycopg2.OperationalError as err:
            h5_log().dbg(f'psycopg2.OperationalError {err.pgerror}')
        except psycopg2.Error as err:
            print(f'Неизвестаная ошибка базы данных {err.pgerror}')
        # во всех остальных случаях, включая exceptions, метод вернет False
        return False

    def _executor(self, sql, params):
        """ Исполнение SQL запроса"""
        self.db.execute_sql(sql, params)

    def _iresponse(self):
        """
        Возвращает итератор ответа
        """
        yield from self.db.get_result()

class DB_Worker(DB):
    """ Класс работы с картами"""

    def __init__(self, con_params):
        """
        Инициализация подключения.
        :param con_params: словарь параметров подключения
        """
        super().__init__(con_params)

    def add_worker(self, params):

        sql = """
                INSERT INTO worker_info (WORKER_LAST_NAME,
                                        WORKER_NAME,
                                        WORKER_MIDDLE_NAME,
                                        WORKER_PASSPORT_SERIES,
                                        WORKER_PASSPORT_ID,
                                        WORKER_POSITION_HELD,
                                        WORKER_PLACE_OF_RESIDENT)
                VALUES (%(WORKER_LAST_NAME)s, 
                        %(WORKER_NAME)s, 
                        %(WORKER_MIDDLE_NAME)s,
                        %(WORKER_PASSPORT_SERIES)s,
                        %(WORKER_PASSPORT_ID)s,
                        %(WORKER_POSITION_HELD)s,
                        %(WORKER_PLACE_OF_RESIDENT)s);"""


        self._executor(sql, params)
        return self._iresponse()


if __name__ == '__main__':

    db = DB_Worker(conn_params)
    print(db.test_connection(conn_params))