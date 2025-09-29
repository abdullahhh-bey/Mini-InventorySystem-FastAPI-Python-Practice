from pydantic import Field, BaseModel
from typing import Optional
from datetime import datetime

class AddProduct(BaseModel):
    
    name: str = Field(description="Name is necessary")
    price : int 
    in_stock : bool
    category : str
    
    

class ProductInfo(BaseModel):
    
    id : int
    name: str = Field(description="Name is necessary")
    price : int 
    in_stock : bool
    category : str
    
    class Config:
        from_attributes = True   # <-- allows returning SQLAlchemy objects
    
    
class UpdateProduct(BaseModel):
    name: str | None = None
    price : int | None = None
    in_stock : bool | None = None
    category : str | None = None
    

class CreateCustomer(BaseModel):
    name : str
    email : str
    
    
class CustomerInfo(BaseModel):
    id : int
    name : str
    email : str
    
    class Config:
        from_attributes = True
        
        
class CreateOrder(BaseModel):
    orderDate : datetime
    customer_id : int


class OrderItemInfo(BaseModel):
    id : int
    order_id : int
    quantity : int
    product : ProductInfo
    
    class Config:
        from_attributes = True
        

class OrderInfo(BaseModel):
    id : int
    orderDate : datetime
    customer_id : int
    order_items : Optional[list[OrderItemInfo]] = []
    
    class Config:
        from_attributes = True
        
 
class CreateOrderItem(BaseModel):
     order_id : int
     quantity : int
     product_id : int
     
     
     
class CustomerWithOrders(BaseModel):
    name : str
    email : str
    orders : Optional[list[OrderInfo]] = []
    
    #mapping
    class Config:
        from_attributes = True
        
