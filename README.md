# Gestion des Clients avec FastAPI et Frontend

Bienvenue dans ce projet qui utilise **FastAPI** pour le backend et un frontend développé en **React**.

## Fonctionnalités

- CRUD des clients (Créer, Lire, Mettre à jour, Supprimer)
- API rapide et performante avec **FastAPI**
- Interface utilisateur moderne en **React**
- Connexion avec une base de données
- CORS activé pour permettre la communication frontend-backend

## Installation et Configuration

### Prérequis

- **Python 3.9+**
- **Node.js 16+** 
- **Git**

### Installation du Backend (FastAPI)

1. Clone le repo :
   ```sh
   git clone https://github.com/ton-utilisateur/ton-repo.git
   cd ton-repo
   ```
2. Crée un environnement virtuel et active-le :
   ```sh
   python -m venv env
   source env/bin/activate  # Sur Mac/Linux
   env\Scripts\activate     # Sur Windows
   ```
3. Installe les dépendances :
   ```sh
   pip install -r requirements.txt
   ```
4. Lance le serveur FastAPI :
   ```sh
   uvicorn main:app --reload
   ```
5. Accède à l'API sur `http://127.0.0.1:8000`
6. Documentation interactive Swagger : `http://127.0.0.1:8000/docs`

### Installation du Frontend


1. Va dans le dossier du frontend :
   ```sh
   cd frontend
   ```
2. Installe les dépendances :
   ```sh
   npm install
   ```
3. Lance l'application :
   ```sh
   npm start  # Pour React
   ```

## Aperçu du Frontend

![Description](Screenshot%202025-03-12%20100611.png)

![Description](Screenshot%202025-03-12%20100635.png)
## Exemples d'utilisation de l'API

### Création d'un client (POST)

#### Requête :

```json
{
  "customer_id": "AZEFG",
  "full_name": "Zakaria Ghanim",
  "company": "VDE",
  "country": "France",
  "city": "SEVRAN"
}
```

#### Réponse :

```json
{
  "message": "Customer added successfully"
}
```
