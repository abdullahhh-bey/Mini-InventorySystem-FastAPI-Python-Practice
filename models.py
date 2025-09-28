from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from db import Base , engine


class Product(Base):
    
    __tablename__= "Products"
    
    id = Column(Integer , primary_key=True)
    name = Column(String(30) , nullable=False)
    price = Column(Integer , nullable=False)
    in_stock = Column(Boolean , default=True)
    category = Column(String(50) , nullable=True)
    
    
class Customer(Base):
    
    __tablename__ = "Customers"
    
    id = Column(Integer , primary_key=True)
    name = Column(String(50) , nullable=False)
    email = Column(String(50) , nullable=False , unique=True)

Base.metadata.create_all(bind=engine)
