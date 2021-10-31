from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmarket

engine = create_engine('mysql+mysqlconnector://<root>:<password>@<host>[:<3306>]/,<Usuarios>')
Session = sessionmarket(bind=engine)
session = Session()

Base = declarative_base()




