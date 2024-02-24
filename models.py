from sqlalchemy import create_engine, Boolean, Integer, Column, ForeignKey, String
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
from os import getenv

load_dotenv()

drivername = str(getenv('drivername'))
hostname = str(getenv('hostname'))
database = str(getenv('db_name'))
username = str(getenv('username'))
password = str(getenv('password'))
port = int(getenv('port'))

url = URL.create(
        drivername=drivername,
        username=username,
        password=password,
        host=hostname,
        database=database,
        port=port
        )

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()
base = declarative_base()

class Note(base):
    __tablename__ = "notes"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False)
    desc = Column(String,nullable=False)
    details = Column(String, nullable=True)

base.metadata.create_all(engine)


