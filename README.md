code pour executer du dashboard steamlist : 
  python -m streamlit run src/dashboard/app.py


syntaxe pour tester et charger les piplenes :
$env:PYTHONPATH="src"
>> python -m pytest


Projet Data Processing — Pipeline Dagster

Pipeline de données de bout en bout avec orchestration Dagster, stockage PostgreSQL / InfluxDB, visualisation Streamlit et conteneurisation Docker.


Table des Matières

Aperçu du Projet
Architecture
Stack Technique
Structure du Projet
Prérequis
Installation & Déploiement
Exécution de la Pipeline
Tests
Monitoring
Choix de Conception
Auteurs


Aperçu du Projet
Ce projet implémente une pipeline ETL complète permettant de :

Extraire des données depuis une API externe (capteurs / IoT)
Transformer et enrichir ces données
Stocker les résultats dans des bases de données relationnelles et séries temporelles
Visualiser les données via un dashboard interactif Streamlit
Orchestrer l'ensemble avec Dagster (assets, jobs, schedules, sensors, partitions)


Architecture
┌─────────────────────────────────────────────────────────────────┐
│                        PIPELINE DAGSTER                         │
│                                                                 │
│   API Externe                                                   │
│       │                                                         │
│       ▼                                                         │
│   extract.py ──► transform.py ──► load.py                      │
│       │                               │                         │
│       │                    ┌──────────┴──────────┐             │
│       │                    ▼                     ▼             │
│       │              PostgreSQL            InfluxDB            │
│       │              (données             (séries              │
│       │               relationnelles)      temporelles)        │
│       │                                                         │
│       └──────────────────────────────────────────────────────► │
│                         Streamlit Dashboard                     │
└─────────────────────────────────────────────────────────────────┘

Orchestration : Dagster (Assets · Jobs · Schedules · Sensors · Partitions)
Infrastructure : Docker Compose (dagster, postgres, influxdb, minio, redis, mongo)

Stack Technique
ComposantTechnologieRôleOrchestrationDagsterGestion de la pipeline ETLStockage relationnelPostgreSQL 15Données structuréesSéries temporellesInfluxDB 2.7Métriques et capteursObject storageMinIOStockage de fichiers / assetsCacheRedisFile de messages, cacheBase documentaireMongoDBDonnées semi-structuréesDashboardStreamlitVisualisationTestspytestTests unitairesConteneurisationDocker / Docker ComposeDéploiement

Structure du Projet
Projet_data_processing/
├── docker/
│   ├── docker-compose.yml       # Orchestration des conteneurs
│   └── Dockerfile               # Image Docker de la pipeline
├── src/
│   ├── dashboard/
│   │   └── app.py               # Dashboard Streamlit
│   └── pipeline/
│       ├── assets/
│       │   ├── extract.py       # Extraction des données (API)
│       │   ├── transform.py     # Transformation et nettoyage
│       │   └── load.py          # Chargement en base de données
│       ├── definitions.py       # Entrée Dagster (assets, jobs, schedules...)
│       ├── jobs.py              # Définition des jobs Dagster
│       ├── schedules.py         # Planification des exécutions
│       ├── sensors.py           # Détection d'événements
│       ├── partitions.py        # Partitionnement des données
│       └── __init__.py
├── tests/
│   ├── test_assets.py           # Tests des assets Dagster
│   └── test_pipeline.py        # Tests d'intégration de la pipeline
├── resources/                   # Ressources partagées (configurations, etc.)
├── pyproject.toml               # Configuration du projet Python
├── requirements.txt             # Dépendances Python
├── .gitignore
└── README.md

Prérequis
Avant de commencer, assurez-vous d'avoir installé :

Docker Desktop ≥ 24.x
Docker Compose ≥ 2.x
Python ≥ 3.10 (pour les tests en local uniquement)
Git


Installation & Déploiement
1. Cloner le dépôt
bashgit clone https://github.com/<votre-utilisateur>/Projet_data_processing_KOMBOU_DJOUKWE.git
cd Projet_data_processing_KOMBOU_DJOUKWE
2. Configurer les variables d'environnement
Créez un fichier .env à la racine du projet (ou dans docker/) :
env# PostgreSQL
POSTGRES_USER=dagster
POSTGRES_PASSWORD=dagster
POSTGRES_DB=pipeline_db

# InfluxDB
INFLUXDB_ADMIN_USER=admin
INFLUXDB_ADMIN_PASSWORD=adminpassword
INFLUXDB_ORG=myorg
INFLUXDB_BUCKET=sensors

# MinIO
MINIO_ROOT_USER=minioadmin
MINIO_ROOT_PASSWORD=minioadmin

# API Externe (à adapter selon votre source)
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com
3. Lancer les conteneurs Docker
bashdocker-compose up --build

Note : Le premier build peut prendre quelques minutes. Les services démarrent dans l'ordre suivant : bases de données → Dagster backend → Dagster UI.

Pour lancer en arrière-plan :
bashdocker-compose up --build -d
4. Accéder aux interfaces
ServiceURLIdentifiantsDagster UIhttp://localhost:3000—Streamlit Dashboardhttp://localhost:8501—InfluxDB UIhttp://localhost:8086admin / adminpasswordMinIO Consolehttp://localhost:9001minioadmin / minioadmin

Exécution de la Pipeline
Via l'interface Dagster

Ouvrir http://localhost:3000
Naviguer dans Assets pour matérialiser les assets manuellement
Naviguer dans Jobs pour lancer un job complet
Les Schedules s'exécutent automatiquement selon la planification définie

Via la ligne de commande
bash# Définir le PYTHONPATH (si exécution locale hors Docker)
$env:PYTHONPATH="src"          # PowerShell (Windows)
export PYTHONPATH="src"        # Bash (Linux / macOS)

# Lancer un job Dagster
dagster job execute -f src/pipeline/definitions.py -j <nom_du_job>
Lancer le Dashboard Streamlit (hors Docker)
bashpython -m streamlit run src/dashboard/app.py

Tests
Les tests unitaires sont écrits avec pytest et couvrent les assets, les transformations et les étapes de chargement.
Exécuter les tests
bash# Définir le PYTHONPATH
$env:PYTHONPATH="src"          # PowerShell
export PYTHONPATH="src"        # Bash

# Lancer tous les tests
python -m pytest

# Avec affichage détaillé
python -m pytest -v

# Lancer un fichier de tests spécifique
python -m pytest tests/test_pipeline.py -v
Couverture de code
bashpython -m pytest --cov=src --cov-report=html
# Rapport disponible dans htmlcov/index.html

Monitoring
Dagster UI
Le tableau de bord Dagster (http://localhost:3000) offre nativement :

Runs : historique de toutes les exécutions avec statut (succès / échec)
Assets : état de matérialisation de chaque asset
Logs : logs détaillés par run avec niveau (INFO, WARNING, ERROR)
Schedules & Sensors : état d'activation et historique des déclenchements

Logs applicatifs
bash# Voir les logs d'un conteneur en temps réel
docker-compose logs -f dagster-1
docker-compose logs -f backend-1

# Voir les logs de tous les services
docker-compose logs -f
Alertes
Les Sensors Dagster (sensors.py) sont configurés pour détecter les anomalies et déclencher des alertes en cas de données manquantes ou d'erreurs lors de l'extraction.

Choix de Conception
Pourquoi Dagster ?
Dagster offre une approche asset-based qui permet de modéliser naturellement les dépendances entre les étapes du pipeline. Le suivi de lignage des données, la gestion native des partitions et l'interface de monitoring intégrée en font un choix idéal pour un projet ETL de bout en bout.
Pourquoi PostgreSQL + InfluxDB ?

PostgreSQL est utilisé pour les données structurées et les métadonnées (fiabilité ACID, requêtes SQL complexes).
InfluxDB est optimisé pour les séries temporelles (données de capteurs horodatées), avec des performances de lecture/écriture bien supérieures à un SGBD relationnel classique pour ce type de données.

Pourquoi Streamlit ?
Streamlit permet de construire rapidement un dashboard interactif en Python, sans avoir besoin de développer un frontend séparé. Il s'intègre naturellement avec pandas, matplotlib et plotly.
Pourquoi Docker ?
La conteneurisation garantit la reproductibilité de l'environnement et simplifie le déploiement. Chaque service est isolé et peut être mis à l'échelle indépendamment.

Arrêter les services
bash# Arrêter les conteneurs
docker-compose down

# Arrêter et supprimer les volumes 
docker-compose down -v

Auteurs
Projet réalisé dans le cadre du cours Data Processing — SupInfo

Mon gitHUB Hector KOMBOU — https://github.com/djouk140/Projet_data_processing/tree/main/data%20processing/projet%20soutenance/Projet_data_processing_KOMBOU_DJOUKWE_Hector
