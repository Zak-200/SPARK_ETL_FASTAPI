from fastapi import APIRouter, Query, HTTPException
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# 🔹 Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["customer_db"]
collection = db["customers"]


# 🔹 Définition du modèle Pydantic
class Customer(BaseModel):
    full_name: str
    company: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    phone_1: Optional[str] = None
    phone_2: Optional[str] = None
    email: EmailStr
    subscription_date: Optional[datetime] = None
    website: Optional[str] = None


router = APIRouter()


# 🔹 1. GET /customers → Liste tous les clients
@router.get("/customers", response_model=List[dict])
def get_customers(
        country: Optional[str] = Query(None, description="Filtrer par pays"),
        company: Optional[str] = Query(None, description="Filtrer par entreprise"),
        skip: int = 0,
        limit: int = 10
):
    query = {}
    if country:
        query["country"] = country
    if company:
        query["company"] = company

    customers = list(collection.find(query, {"_id": 0}).skip(skip).limit(limit))
    return customers


# 🔹 2. GET /customers/{customer_id} → Récupérer un client par ID
@router.get("/customers/{customer_id}", response_model=dict)
def get_customer_by_id(customer_id: str):
    if not ObjectId.is_valid(customer_id):
        raise HTTPException(status_code=400, detail="ID invalide")

    customer = collection.find_one({"_id": ObjectId(customer_id)}, {"_id": 0})
    if not customer:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return customer


# 🔹 3. POST /customers → Ajouter un client
from fastapi import Request

@router.post("/customers", response_model=dict)
async def create_customer(request: Request, customer: Customer):
    """
    Ajoute un nouveau client dans la base de données.
    """
    body = await request.json()  # Lire les données envoyées
    print("Données reçues :", body)  # Log pour voir les données

    existing_customer = collection.find_one({"customer_id": customer.customer_id})
    if existing_customer:
        raise HTTPException(status_code=400, detail="Un client avec cet ID existe déjà")

    collection.insert_one(customer.dict())
    return {"message": "Client ajouté avec succès", "customer": customer.dict()}


# 🔹 4. PUT /customers/{customer_id} → Mettre à jour un client
@router.put("/customers/{customer_id}", response_model=dict)
def update_customer(customer_id: str, updated_customer: Customer):
    if not ObjectId.is_valid(customer_id):
        raise HTTPException(status_code=400, detail="ID invalide")

    result = collection.update_one({"_id": ObjectId(customer_id)}, {"$set": updated_customer.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Client non trouvé")

    return {"message": "Client mis à jour avec succès"}


# 🔹 5. DELETE /customers/{customer_id} → Supprimer un client
@router.delete("/customers/{customer_id}", response_model=dict)
def delete_customer(customer_id: str):
    if not ObjectId.is_valid(customer_id):
        raise HTTPException(status_code=400, detail="ID invalide")

    result = collection.delete_one({"_id": ObjectId(customer_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Client non trouvé")

    return {"message": "Client supprimé avec succès"}
