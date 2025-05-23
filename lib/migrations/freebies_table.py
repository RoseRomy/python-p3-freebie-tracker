from sqlalchemy import create_engine
from lib.models import Base, Dev, Company, Freebie  # import all models!

engine = create_engine('sqlite:///freebies.db')
Base.metadata.create_all(engine)

print("Tables created successfully!")
