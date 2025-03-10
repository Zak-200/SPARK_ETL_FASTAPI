from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import customers

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://10.0.200.15:3000",  # Ajoute ton IP locale
    ],
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP
    allow_headers=["*"],  # Autoriser tous les headers
)

# Include your router
app.include_router(customers.router)



