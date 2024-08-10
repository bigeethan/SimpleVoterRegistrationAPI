from sqlalchemy import Boolean, Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

DATABASE_URL = 'postgresql://postgres:therealbige9@localhost:5432/voterregistration'
engine = create_engine(DATABASE_URL)
session = Session(engine)

Base = declarative_base()

class User(Base):
     __tablename__ = 'voters'
     id = Column(Integer, primary_key=True, autoincrement=True)
     is_active = Column(Boolean, default=True)
     first_name = Column(String(256), nullable=False)
     last_name = Column(String(256), nullable=False)
     dob = Column(Integer, nullable=False)
     phone = Column(Integer, nullable=False)
     address = Column(String(256), nullable=False)
     town = Column(String(256), nullable=False)
     state = Column(String(256), nullable=False)
     party = Column(String(256), nullable=False)

# Create the table
Base.metadata.create_all(bind=engine)
print('Tables created.')
session.close()