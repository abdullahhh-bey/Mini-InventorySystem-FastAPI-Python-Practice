from fastapi import FastAPI , HTTPException, Depends 
from models import AddUser , UserInfo
from userService import UserService

#just created app
app = FastAPI()

# #Simple for testing
# # @app.get("/test")
# # async def greet():
# #     return {"message" : "Hello, Alex"}

# # #Path parameter
# # @app.get("/test/{id}")
# # async def get_Id(id : int):
# #     return {"id" : id}


# # #Decorators for Routing
# # #Path parameter
# # @app.get("/square/{n}")
# # async def square_Number(n : int):
# #     n = n**2
# #     return {"endpoint" : "square",
# #             "number" : n
# #             }
    
# # #querey parameter
# # @app.get("/calculate")
# # async def sum_Number(n : int):
# #     return {
# #         "endpoint" : "calculate",
# #         "number" : n+n
# #     }
    
    
# user_list: list[UserInfo] = []

# user_id = 1

# @app.get("/users", response_model=list[UserInfo])
# async def get_users():
#     global user_list
#     return user_list


# @app.post("/users" , response_model=UserInfo)
# async def add_user(user : AddUser):
#     global user_list
#     global user_id
    
#     user_id += 1
    
#     new = UserInfo (
#         id = user_id,
#         name = user.name,
#         email = user.email
#     )
    
#     user_list.append(new)
#     return new

#add singleton method ( made a global instace of this service )
userService = UserService()

#registering UserService
def _userService() -> UserService:
    return userService

@app.get("/users" , response_model=list[UserInfo])
async def getUsers(userService: UserService = Depends(_userService)) -> list[UserInfo]:
    return userService.get_users()

    
@app.get("/users/{id}" )
async def getUserById(id : int , userService: UserService = Depends(_userService)):
    user = userService.get_user_by_id(id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return user 


@app.post("/users", response_model=UserInfo)
async def addUser( user  : AddUser , userService: UserService = Depends(_userService)) -> UserInfo:
    u = userService.add_user(user)
    return u
    
