import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('postgresql+psycopg2://postgres:1@localhost/publishing_company', echo=True)
pool_recycle = 7200

# class Clients():
# 	def __init__(self, nclient_name, client_last_name, client_middle_name, client_phone_number):
# 		self.client_name = client_name
# 		self.client_last_name = client_last_name
# 		self.client_middle_name = client_middle_name
# 		self.client_phone_number = client_phone_number
# 	def __repr__(self):
# 		return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

clients = sa.table('clients', 
	sa.column('client_id'),
	sa.column('client_name'),
	sa.column('client_last_name'),
	sa.column('client_middle_name'),
	sa.column('client_phone_number')
	)

Session = sessionmaker(bind=engine)
session = Session()
ourUser = session.query(clients)
print('ourUser=',ourUser, 'client=', str(clients))
for i in ourUser:
	print(i)
#############################
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(
    'postgresql+psycopg2://postgres:1@localhost:5432/test', echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)


# Создание таблицы
Base.metadata.create_all(engine)

