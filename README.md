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

## Kubernetes Deployment

### Deploying Components
Run the following command to apply all Kubernetes manifests:

```
kubectl apply -f k8s/
```

### Accessing Services

#### Airflow Webserver
To access the Airflow webserver, use the following command to forward the port:

```
kubectl port-forward service/airflow-webserver 8080:8080
```

Then, navigate to `http://localhost:8080` in your browser.

#### Grafana Dashboard
To access the Grafana dashboard, use the following command to forward the port:

```
kubectl port-forward service/grafana 3000:3000
```

Then, navigate to `http://localhost:3000` in your browser.

## Pipeline Execution

### Triggering the Airflow DAG
1. Open the Airflow webserver.
2. Navigate to the `data_pipeline` DAG.
3. Trigger the DAG manually to start the pipeline.

### Verifying dbt Transformations
Check the logs of the `transform_data` task in the Airflow webserver to ensure dbt transformations are executed successfully.

## Monitoring

### Prometheus
Prometheus is configured to scrape metrics from Kubernetes and application components. Access Prometheus using:

```
kubectl port-forward service/prometheus 9090:9090
```

Navigate to `http://localhost:9090` in your browser.

### Grafana
Grafana dashboards are preconfigured to visualize metrics from Prometheus. Use the Grafana dashboard to monitor system health and performance.
