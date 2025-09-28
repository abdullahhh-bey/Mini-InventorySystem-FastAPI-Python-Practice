from pydantic import Field, BaseModel

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
    
