#!/usr/bin/env bash
set -euo pipefail

kind create cluster --config kind-config.yaml
kubectl create namespace airflow

helm repo add apache-airflow https://airflow.apache.org
helm repo update

helm install airflow apache-airflow/airflow \
  --namespace airflow \
  -f helm/values-airflow.yaml \
  --timeout 10m

echo "Run: kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow"
