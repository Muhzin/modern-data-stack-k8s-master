# Modern Data Stack on Kubernetes

This project demonstrates a Modern Data Stack deployed on Kubernetes with:
- Airflow
- dbt
- PostgreSQL
- Metabase

## Architecture

![Architecture Diagram](architecture.png)

## Prerequisites
- Docker
- Kubernetes cluster
- Helm

## Setup
1. Clone this repository
2. Run `docker-compose up -d`
3. Apply Kubernetes manifests

## Environment Variables

### dbt Configuration
Create a `.env` file in the root of the project with the following content:

```
POSTGRES_HOST=localhost
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
```

This file is required for dbt to connect to the PostgreSQL database. Ensure that the `.env` file is not committed to version control by keeping it in `.gitignore`.
