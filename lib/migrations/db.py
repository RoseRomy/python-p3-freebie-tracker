from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base

DATABASE_URL = "sqlite:///freebies.db"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
