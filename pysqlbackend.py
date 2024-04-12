import sql_operation
import models 
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Any


app = FastAPI()

origins = [
    "http://localhost:8080",  # Allow your local website
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#uvicorn pysqlbackend:app --reload

@app.post("/hello_post/")
def hello_post(t:models.test):
    # print("-------------input:" + name)
    return "hello"







@app.get("/hello_get/")
def hello_get():
    return {"message": "Hello World"}

@app.post("/getInfo/")
def getInfo(info:models.tableInfo):
    return sql_operation.getInfo(info)

@app.post("/insertcategory/")
def insert(info:models.category):
    return sql_operation.insertcategory(info)

@app.post("/insertcustomers/")
def insert(info:models.customers):
    return sql_operation.insertcustomers(info)

@app.post("/insertorderdetail/")
def insert(info:models.orderdetail):
    return sql_operation.insertorderdetail(info)

@app.post("/insertorder/")
def insert(info:models.orders):
    return sql_operation.insertorder(info)

@app.post("/insertpici/")
def insert(info:models.pici):
    return sql_operation.insertpici(info)

@app.post("/insertproducts/")
def insert(info:models.products):
    return sql_operation.insertproducts(info)

@app.post("/insertproinfo/")
def insert(info:models.category):
    return sql_operation.insertcategory(info)

@app.post("/insertrule/")
def insert(info:models.rule):
    return sql_operation.insertrules(info)

@app.post("/insertshippers/")
def insert(info:models.shippers):
    return sql_operation.insertshippers(info)

@app.post("/insertsuppliers/")
def insert(info:models.suppliers):
    return sql_operation.insertsuppliers(info)

@app.post("/delete")
def remove(info:models.tableInfo):
    return sql_operation.removeInfo(info)

@app.post("/countorderproducts")
def countorder(info:models.countorderproduct):
    return sql_operation.count_order_product(info)





         