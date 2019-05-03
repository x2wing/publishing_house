import sqlalchemy as sa
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker


class DB():
	config = {'db.url':'postgresql+psycopg2://postgres:1@localhost/publishing_company', 'db.echo':'False' }
	
	def __init__(self):
		engine = engine_from_config(DB.config, prefix='db.')
		Session = sessionmaker(bind=engine)
		self.session = Session()
		# pool_recycle = 7200


class Clients(DB):
	def __init__(self):
		super().__init__()
		self.init_db()

	def init_db(self):
		self.clients = sa.table('clients', 
					sa.column('client_id'),
					sa.column('client_name'),
					sa.column('client_last_name'),
					sa.column('client_middle_name'),
					sa.column('client_phone_number')
					)
	def get_data(self):
		return self.session.query(self.clients)

if __name__ == '__main__':
	print(list(Clients().get_data()))
	