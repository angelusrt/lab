#!/usr/bin/env bash
set -euo pipefail

helm uninstall airflow -n airflow || true
kubectl delete namespace airflow --ignore-not-found
kind delete cluster --name lab
