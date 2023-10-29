from enum import auto
from sqlalchemy import MetaData, create_engine
from sqlalchemy import Table, Integer, String, Column

engine = create_engine('sqlite:///practice/db.sqlite')
meta = MetaData()
conn = engine.connect()

words = Table(
    'words',
    meta,
    Column('id',Integer, primary_key=True, autoincrement=True),
    Column('word',String),
    Column('count', Integer),
    Column('filename',String)
)

#Clear data base
try:
    words.drop(engine)
except:
    pass


meta.create_all(engine)

#Add records
record = words.insert().values(word='hi',count=1,filename='somepic.jpg')
conn.execute(record)