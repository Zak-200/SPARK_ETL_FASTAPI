from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from bson import ObjectId
from pydantic import BaseModel, EmailStr
from typing import Optional



class Customer(BaseModel):
    customer_id: str
    full_name: str
    company: Optional[str]
    city: Optional[str]
    country: Optional[str]
    phone_1: Optional[str]
    phone_2: Optional[str]
    email: EmailStr
    subscription_date: Optional[str]
    website: Optional[str]

router = APIRouter()
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["customer_db"]  # Base de données MongoDB
collection = db["customers"]  # Collection des clients

from typing import List, Optional
# 🔹 1. GET /customers → Liste tous les clients avec pagination facultative
@router.get("/customers", response_model=List[dict])
def get_customers(
    country: Optional[str] = Query(None, description="Filtrer par pays"),
    company: Optional[str] = Query(None, description="Filtrer par entreprise"),
    skip: int = 0,  # Pagination : nombre d'éléments à sauter
    limit: int = 10  # Nombre maximum d'éléments retournés
):
    """
    Récupère la liste des clients avec filtres optionnels sur le pays et l'entreprise.
    """
    query = {}
    if country:
        query["country"] = country
    if company:
        query["company"] = company

    customers = list(collection.find(query))  # Récupère tous les clients sauf `_id`
    print(customers)
    return customers


# 🔹 2. GET /customers/{customer_id} → Récupère un client spécifique
@router.get("/customers/{customer_id}", response_model=dict)
def get_customer_by_id(customer_id: str):
    """
    Récupère un client par son ID unique.
    """
    customer = collection.find_one({"customer_id": customer_id}, {"_id": 0})
    if not customer:
        raise HTTPException(status_code=404, detail="Client non trouvé")
    return customer


# 🔹 3. GET /countries → Nombre de clients par pays
@router.get("/countries", response_model=dict)
def get_customers_by_country():
    """
    Renvoie le nombre de clients par pays.
    """
    pipeline = [
        {"$group": {"_id": "$country", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    result = list(collection.aggregate(pipeline))
    return {"countries": result}


# 🔹 4. GET /companies → Nombre de clients par entreprise
@router.get("/companies", response_model=dict)
def get_customers_by_company():
    """
    Renvoie la liste des entreprises et le nombre de clients associés.
    """
    pipeline = [
        {"$group": {"_id": "$company", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}
    ]
    result = list(collection.aggregate(pipeline))
    return {"companies": result}


# 🔹 5. POST /customers → Ajouter un nouveau client
@router.post("/customers", response_model=dict)
def create_customer(customer: Customer):
    """
    Ajoute un nouveau client dans la base de données.
    """
    existing_customer = collection.find_one({"customer_id": customer.customer_id})
    if existing_customer:
        raise HTTPException(status_code=400, detail="Un client avec cet ID existe déjà")

    collection.insert_one(customer.dict())
    return {"message": "Client ajouté avec succès", "customer": customer.dict()}


# 🔹 6. PUT /customers/{customer_id} → Mettre à jour un client
@router.put("/customers/{customer_id}", response_model=dict)
def update_customer(customer_id: str, updated_customer: Customer):
    """
    Met à jour un client existant dans la base de données.
    """
    result = collection.update_one({"customer_id": customer_id}, {"$set": updated_customer.dict()})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Client non trouvé")

    return {"message": "Client mis à jour avec succès", "customer": updated_customer.dict()}


# 🔹 7. DELETE /customers/{customer_id} → Supprimer un client
@router.delete("/customers/{customer_id}", response_model=dict)
def delete_customer(customer_id: str):
    """
    Supprime un client de la base de données.
    """
    print(f"Deleting customer with ID: {customer_id}")  # Log the ID
    result = collection.delete_one({"customer_id": customer_id})  # Use "customer_id" instead of "Customer Id"
    if result.deleted_count == 0:
        print(f"Customer with ID {customer_id} not found")  # Log if customer not found
        raise HTTPException(status_code=404, detail="Client non trouvé")

    print(f"Customer with ID {customer_id} deleted successfully")  # Log success
    return {"message": "Client supprimé avec succès"}