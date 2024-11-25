from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

# class Base(DeclarativeBase):
#     pass

# user = 'postgres'
# password = 'your_password'
# host = 'localhost'
# port = '5432'
# database = 'mydb'

# connection_str = f"postgresql:// {user}:{password}@{host}:{port}/{database}"
# engine = create_engine(connection_str)

# engine = create_engine(connection_str)
# you can test if the connection is made or not

# engine = create_engine("sqlite+pysqlite:///aspp.db", echo=True)
user = 'docker'
password = 'docker'
host = 'localhost'
# host = '0.0.0.0'
# host = '5432'
port = '5432'
database = 'student_management_db'
# connection_str = f"postgresql:// {user}:{password}@{host}:{port}/{database}"
engine = create_engine('postgresql://docker:docker@localhost:5432/student_management_db')
# engine = create_engine(connection_str)

"""
name: management_db
host name/address: localhost
port: 5432
username: postgres_mng

"""

try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')

# engine = create_engine("sqlite+pysqlite:///apsp.db", echo=True)

# engine = create_engine(dialect+driver://username:password@host:port/database_name)
# engine = create_engine('postgresql+psycopg2://user:password@hostname/database_name')

print("creating base")
# Base.metadata.create_all(engine) # create table

db_session = Session(bind=engine)

#  name: std_mng_sys
#  hostname: stdmng
#  user: postgres
# Please enter the password for the user 'postgres' to connect the server - "PostgreSQL 14"
#  port: 5432
#  123456