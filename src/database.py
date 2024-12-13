from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase


# user = 'docker'
user = "postgres"
password = 'docker'
host = 'localhost'
port = '5432'
database = 'student_management_db'
engine = create_engine('postgresql://docker:docker@127.0.0.1:5432/student_management_db')
# connection_str = f"postgresql:// {user}:{password}@{host}:{port}/{database}"
# engine = create_engine(connection_str)

try:
    with engine.connect() as connection_str:
        print('Successfully connected to the PostgreSQL database')
except Exception as ex:
    print(f'Sorry failed to connect: {ex}')

print("creating base")

db_session = Session(bind=engine)