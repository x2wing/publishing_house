from abc import abstractmethod

import sqlalchemy as sa
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker


class DB():
    config = {'db.url': 'postgresql+psycopg2://postgres:1@localhost/publishing_company', 'db.echo': 'True'}

    def __init__(self):
        engine = engine_from_config(DB.config, prefix='db.')
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.init_db()

    # pool_recycle = 7200

    @abstractmethod
    def init_db(self):
        pass

    def get_data(self):
        return self.session.query(self.t)

class Clients(DB):
    def __init__(self):
        super().__init__()

    def init_db(self):
        self.clients = sa.table('clients',
                                sa.column('client_id'),
                                sa.column('client_name'),
                                sa.column('client_last_name'),
                                sa.column('client_middle_name'),
                                sa.column('client_phone_number')
                                )





class Supply(DB):
    def __init__(self):
        super().__init__()

    def init_db(self):
        self.t = sa.table('supply',
                                sa.column('provider_id'),
                                sa.column('supply_date_and_time'),
                                )

    def get_data(self):
        return self.session.query(self.t.client_id)

    def get_obj(self):
        print(repr(self.t))
        return self.t

if __name__ == '__main__':
    print(Supply().get_obj())
