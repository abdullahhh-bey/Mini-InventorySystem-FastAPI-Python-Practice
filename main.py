from fastapi import FastAPI , HTTPException, Depends 
from db import get_db
from dtos import ProductInfo , AddProduct, UpdateProduct , CustomerInfo, CreateCustomer, OrderInfo, CreateOrder, OrderItemInfo, CreateOrderItem
from sqlalchemy.orm import Session
from models import Product , Customer , Order, OrderItems


#defined the connection string to SQLITE 


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
# userService = UserService()

# #registering UserService
# def _userService() -> UserService:
#     return userService

# @app.get("/users" , response_model=list[UserInfo])
# async def getUsers(userService: UserService = Depends(_userService)) -> list[UserInfo]:
#     return userService.get_users()

    
# @app.get("/users/{id}" )
# async def getUserById(id : int , userService: UserService = Depends(_userService)):
#     user = userService.get_user_by_id(id)
#     if not user:
#         raise HTTPException(
#             status_code=404,
#             detail="User not found"
#         )
#     return user 


# @app.post("/users", response_model=UserInfo)
# async def addUser( user  : AddUser , userService: UserService = Depends(_userService)) -> UserInfo:
#     u = userService.add_user(user)
#     return u
    
# @app.delete("/users/{id}")
# async def removeUser(id : int, userService: UserService = Depends(_userService)):
#     u = userService.remove_user(id)
#     return u


@app.get("/products" , response_model=list[ProductInfo])
async def getProduct(db : Session = Depends(get_db)):
    products = db.query(Product).all()
    return  products



@app.post("/products" , response_model=ProductInfo)
async def createProduct( p : AddProduct , db : Session = Depends(get_db)) -> ProductInfo:
    pro = db.query(Product).filter(Product.name == p.name).first()
    
    if pro:
        raise HTTPException(
            status_code=400,
            details="Email already exists"
        )
    
    new_product =  Product(
        name = p.name,
        price = p.price,
        in_stock = True,
        category = p.category
    )
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product



@app.get("/products/{id}" , response_model=ProductInfo)
async def getProductById(id : int , db : Session = Depends(get_db)) -> ProductInfo:
    p = db.query(Product).filter(Product.id == id).first()
    if not p:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )
    return p


@app.put("/products/{id}", response_model=ProductInfo)
async def update_product(id: int, product: UpdateProduct, db: Session = Depends(get_db)):
    p = db.query(Product).filter(Product.id == id).first()
    if not p:
        raise HTTPException(status_code=404, detail="Product not found")

    if product.name is not None:
        p.name = product.name
    if product.price is not None:
        p.price = product.price
    if product.in_stock is not None:
        p.in_stock = product.in_stock
    if product.category is not None:
        p.category = product.category

    db.commit()
    db.refresh(p)
    return p


@app.delete("/products/{id}")
async def removeUser(id : int , db: Session = Depends(get_db)):
    p = db.query(Product).filter(Product.id == id).first()
    if p is None:
        raise HTTPException(
            status_code=404,
            details="Product not found"
        )
        
    db.delete(p)
    db.commit()
    return f"User:{id} removed"


@app.get("/products/sort/{price}")
async def getProductsByPrice( price : int , db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.price > price).all()
    
    if not products:
        raise HTTPException(
            status_code=404,
            detail="No Product found")
        
    return products


@app.get("/products/sort-by-type/{category}")
async def getProductByType(category : str , db: Session = Depends(get_db)):
    products = db.query(Product).filter(Product.category == category).all()
    
    if not products:
        raise HTTPException(
            status_code=404,
            detail="No Product found"
        )
        
    return products



#start here 
@app.post("/customers" , response_model=CustomerInfo)
async def AddCustomer( c : CreateCustomer ,db: Session = Depends(get_db)) -> CustomerInfo:
    check = db.query(Customer).filter(Customer.email == c.email).first()
    if check:
        raise HTTPException(
            status_code=400,
            detail="Email already exist!"
        )
        
    new_customer = Customer(
        name = c.name,
        email = c.email
    )
    
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer



@app.get("/customers", response_model=list[CustomerInfo])
async def getCustomers(db: Session = Depends(get_db)) -> list[CustomerInfo]:
    c = db.query(Customer).all()
    if not c:
        raise HTTPException(
            status_code=404,
            detail="No Customers"
        )
        
    return c


@app.get("/customers/{id}" , response_model=CustomerInfo)
async def getCustomerById(id : int , db: Session = Depends(get_db)) -> CustomerInfo:
    c = db.query(Customer).filter(Customer.id == id).first()
    if c is None:
        raise HTTPException(
            status_code=404,
            detail="No Customer"
        )
    
    return c



@app.post("/orders" , response_model=OrderInfo)
async def AddOrder( order : CreateOrder ,db: Session = Depends(get_db)) -> OrderInfo:
    check = db.query(Customer).filter(Customer.id == order.customer_id).first()
    if check is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not exist"
        )
        
    new_order = Order(
        orderDate = order.orderDate,
        customer_id = order.customer_id
    )
    
    db.add(new_order)
    db.commit()
    db.refresh(new_order)
    return new_order



@app.get("/orders" , response_model=list[OrderInfo])
async def getOrder(db: Session = Depends(get_db)) -> list[OrderInfo]:
    o = db.query(Order).all()
    if not o:
        raise HTTPException(
            status_code=404,
            detail="No Orders yet"
        )
    return o



@app.post("/orderItems" , response_model=OrderItemInfo)
async def AddOrderItem( o : CreateOrderItem ,db: Session = Depends(get_db)) -> OrderItemInfo:
    orderCheck = db.query(Order).filter(Order.id == o.order_id).first()
    if orderCheck is None:
        raise HTTPException(
            status_code=404,
            detail="No Order found with this id"
        )
        
    productCheck = db.query(Product).filter(Product.id == o.product_id).first()
    if productCheck is None:
        raise HTTPException(
            status_code=404,
            detail="No Product found with this id"
        )
        
    orderItem = OrderItems(
        quantity = o.quantity,
        order_id = o.order_id,
        product_id = o.product_id
    )
    
    db.add(orderItem)
    db.commit()
    db.refresh(orderItem)
    return orderItem
    


@app.get("/orderItems" , response_model=list[OrderItemInfo])
async def getOrderItems(db: Session = Depends(get_db)) -> list[OrderItemInfo]:
    items = db.query(OrderItems).all()
    if not items:
        raise HTTPException(
            status_code=404,
            detail="No Order Items yet"
        )
    return items