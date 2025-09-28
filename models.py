from pydantic import BaseModel, Field, EmailStr

class AddUser(BaseModel):
    name : str = Field(... , min_length=3 , max_length=30, description="Enter full name")
    email : EmailStr = Field(..., description="Enter valid email")
    password : str = Field(... , min_length=7 , max_length=20, description="Enter valid password" )
    
class UserInfo(BaseModel):
    id : int
    name : str
    email : EmailStr
    
