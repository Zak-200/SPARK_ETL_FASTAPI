# README - Pipeline ETL & API FastAPI avec ReactJS

## Objectif
Mettre en place un pipeline ETL pour traiter un fichier CSV contenant des informations clients, stocker ces données dans MongoDB et exposer ces informations via une API FastAPI. L'interface ReactJS permettra de visualiser les données sous forme de tableau et de graphiques interactifs, ainsi que d'effectuer des opérations CRUD.

## Planning de Développement

### Mise en place du pipeline ETL
- Installation et configuration de l'environnement (Python, MongoDB, Airflow).
- Lecture et extraction des données depuis le fichier CSV.
- Transformation des données (nettoyage, jointure, agrégation).
- Chargement des données dans MongoDB.

### Développement de l'API FastAPI
- Création de l'API FastAPI avec les endpoints `GET`, `POST`, `PUT`, `DELETE`.
- Implémentation de la logique de filtrage et de recherche (par pays, entreprise).
- Tests de l'API et gestion des erreurs.

### Développement de l'interface ReactJS
- Mise en place de l'application React et affichage des données sous forme de tableau dynamique.
- Création des graphiques interactifs (Chart.js/Recharts) pour le dashboard.
- Implémentation du formulaire CRUD (ajouter, modifier, supprimer un client).

### Finalisation et Tests
- Tests d'intégration entre le front-end, l'API et la base de données MongoDB.
- Déploiement local de l'application.
- Documentation et amélioration de l'interface utilisateur.
- Optionnel : Dockerisation pour le déploiement.

## Prérequis
- Python 3.10
- MongoDB
- React 18
- Docker 
