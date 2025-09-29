from pydantic import Field, BaseModel
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
    

class OrderInfo(BaseModel):
    id : int
    orderDate : datetime
    customer_id : int
    customer : CustomerInfo
    
    class Config:
        from_attributes = True
        
 