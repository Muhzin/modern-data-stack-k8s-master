.PHONY: up down psql

up:
docker-compose up -d

down:
docker-compose down

psql:
docker exec -it modern-data-stack-k8s-master-postgres-1 psql -U airflow
