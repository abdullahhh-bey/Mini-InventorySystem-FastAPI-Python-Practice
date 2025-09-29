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
        orm_mode = True   # <-- allows returning SQLAlchemy objects
    
    
class UpdateProduct(BaseModel):
    name: str | None = None
    price : int | None = None
    in_stock : bool | None = None
    category : str | None = None
    



class CreateOrder(BaseModel):
    total_amount : int
    order_date : datetime
    customer_id : int


class CreateCustomer(BaseModel):
    name : str
    email : str
    
    

class CustomerResponse(BaseModel):
    id : int
    name : str
    email : str
    
    class Config:
        orm_mode = True
        
        
class OrderResponse(BaseModel):
    id : int
    orderDate : datetime
    
    class Config:
        orm_mode = True
        
        
class CustomerWithOrder(BaseModel):
    id : int
    name : str
    email : str
    
    orders : list[OrderResponse] 
    
    class Config:
        orm_true = True
    

class OrderWithCustomer(BaseModel):
    id : int
    orderDate : datetime
    customer : CustomerResponse
    
    class Config:
        orm_true = True