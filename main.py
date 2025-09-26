from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def greet():
    return {"message" : "Hello, Alex"}

@app.get("/test/{id}")
async def get_Id(id : int):
    return {"id" : id}


#Decorators for Routing
@app.get("/square/{n}")
async def square_Number(n : int):
    n = n**2
    return {"endpoint" : "square",
            "number" : n
            }
    
#querey parameter
@app.get("/calculate")
async def sum_Number(n : int):
    return {
        "endpoint" : "calculate",
        "number" : n+n
    }
    
    
 
