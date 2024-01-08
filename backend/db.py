import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ["DATABASE_USERNAME"]}:{os.environ["DATABASE_PASSWORD"]}@{os.environ["DATABASE_HOST"]}:{os.environ["DATABASE_PORT"]}/{os.environ["DATABASE_NAME"]}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
