from trash.orm_example import CData, Engine

from sqlalchemy import MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker




# начинаем новую сессию работы с БД
Session = sessionmaker(bind=Engine().db_engine)
session = Session()

# таким образом можно добавить новый элемент
new_element = CData("http://blog.com", "http://coolpix.com/img434.jpg", "Nice Post", "Mark spomoni as a faggot")
session.add(new_element)

# посмотрим что уже есть в базе данных
for instance in session.query(CData).order_by(CData.id):
    print(instance.title)

# совершаем транзакцию
session.commit()