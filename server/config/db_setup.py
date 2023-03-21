from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import dotenv_values

config = dict(dotenv_values(".env"))

user = config.get('USER')
password = config.get('PASSWORD')
server = config.get('SERVER')
db = config.get('DB')

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{server}/{db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, future=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
