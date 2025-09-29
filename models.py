from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from db import Base , engine
from sqlalchemy.orm import relationship


class Product(Base):
    
    __tablename__= "Products"
    
    id = Column(Integer , primary_key=True)
    name = Column(String(30) , nullable=False)
    price = Column(Integer , nullable=False)
    in_stock = Column(Boolean , default=True)
    category = Column(String(50) , nullable=False)

    order_item = relationship("OrderItems" , back_populates="product")
    
    

class OrderItems(Base):

    __tablename__ = "Order_Items"
    
    id = Column(Integer , primary_key=True)
    quantity = Column(Integer , nullable=False, default=1)
    
    order_id = Column(Integer, ForeignKey("Orders.id"))
    order = relationship("Order" , back_populates="order_items")
    
    product_id = Column(Integer , ForeignKey("Products.id"))
    product = relationship("Product" , back_populates="order_item")

    
    
class Order(Base):
    
    __tablename__ = "Orders"
    
    id = Column(Integer , primary_key=True)
    orderDate = Column(DateTime , nullable=False)
    
    customer_id = Column(Integer, ForeignKey("Customers.id"))
    customer = relationship("Customer" , back_populates="orders")
    
    order_items = relationship("OrderItems" , back_populates="order")
    

        
    
class Customer(Base):
    
    __tablename__ = "Customers"
    
    id = Column(Integer , primary_key=True)
    name = Column(String(50) , nullable=False)
    email = Column(String(50) , nullable=False , unique=True)  
      
    orders = relationship("Order" , back_populates="customer")

Base.metadata.create_all(bind=engine)
