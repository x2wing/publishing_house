from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine(
    'postgresql+psycopg2://postgres:1@localhost:5432/publishing_company', echo=False)
Base = declarative_base()

class Supply(Base):
    __tablename__ = 'supply'
    provider_id = Column(Integer)
    supply_date_and_time = Column(TIMESTAMP)


    def __init__(self, provider_id, supply_date_and_time):
        self.provider_id = provider_id
        self.supply_date_and_time = supply_date_and_time


    def __repr__(self):
        return "<User('%s','%s')>" % (self.provider_id, self.supply_date_and_time)

if __name__ == '__main__':
    Session = sessionmaker(bind=engine)
    session = Session()
    ourUser = session.query(Supply)
    # print(ourUser)
    for i in ourUser:
        print(i)
        # i=list(i)
        # print({i[0]:i[1]})