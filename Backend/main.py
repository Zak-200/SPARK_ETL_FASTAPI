from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["customer_db"]
collection = db["customers"]

@app.get("/customers")
def get_customers():
    customers = list(collection.find({}, {"_id": 0}))
    return {"customers": customers}

@app.get("/customers/{customer_id}")
def get_customer(customer_id: str):
    customer = collection.find_one({"Customer Id": customer_id}, {"_id": 0})
    return {"customer": customer}

@app.get("/countries")
def get_countries():
    pipeline = [
        {"$group": {"_id": "$Country", "count": {"$sum": 1}}}
    ]
    countries = list(collection.aggregate(pipeline))
    return {"countries": countries}

@app.post("/customers")
def add_customer(customer: dict):
    collection.insert_one(customer)
    return {"message": "Customer added"}

@app.put("/customers/{customer_id}")
def update_customer(customer_id: str, customer: dict):
    collection.update_one({"Customer Id": customer_id}, {"$set": customer})
    return {"message": "Customer updated"}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str):
    collection.delete_one({"Customer Id": customer_id})
    return {"message": "Customer deleted"}
