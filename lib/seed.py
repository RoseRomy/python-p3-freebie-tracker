from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')
Session = sessionmaker(bind=engine)
session = Session()

# Optional: Clear old data
session.query(Freebie).delete()
session.query(Dev).delete()
session.query(Company).delete()
session.commit()

# Create Companies
c1 = Company(name="TechCorp", founding_year=2000)
c2 = Company(name="CodeWorks", founding_year=2010)

# Create Devs
d1 = Dev(name="Alice")
d2 = Dev(name="Bob")

# Create Freebies
f1 = Freebie(item_name="T-shirt", value=15, dev=d1, company=c1)
f2 = Freebie(item_name="Sticker", value=2, dev=d1, company=c2)
f3 = Freebie(item_name="Mug", value=10, dev=d2, company=c1)

session.add_all([c1, c2, d1, d2, f1, f2, f3])
session.commit()

print("Seed data added!")
