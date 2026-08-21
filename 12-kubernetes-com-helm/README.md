# Kubernetes com Helm

Antes de tudo, por quê Kubernetes?

O propósito do Kubernetes é provisionar infraestrutura "permanente" que necessita de escalabilidade, mas que nunca escalará para 0. 

Outros benefícios são:
- Portabilidade
- Multicloud
- Orquestrar microserviços como se fosse um
- "Pureza arquitetural"

Em Kubernetes, nós lidamos com 'pods' que são containers substutíveis com rede e etc.

Helm, por outro lado, é um gerenciador de pacotes que instala 'charts', que são pastas que contém templates de serviços. 

Para conseguirmos fazer qualquer coisa com Kubernetes é necessário o cliente (kubectl) e um provedor, podendo ser:
- kind (Kubernetes IN Docker)
- minikube (single VM)
- k3s (prod)
- k8 (prod)

Tipicamente, você possui dois arquivos YAML:
- deployment.yaml - define como a aplicação roda (Dockerfile é citado aqui)
- service.yaml - define como outros componentes acessam a aplicação

Como usar? Assim:
- "kubectl apply -f k8s/deployment.yaml"
- "kubectl apply -f k8s/service.yaml"

É possível ter mais arquivos, mas esse é o básico.

Já, com o Helm, você consegue instalar um template de um projeto e usá-lo com um arquivo 'values.yaml' para configurar aquela infra pronta. 
Se você quiser editar, você usaria 'helm pull <project> --untar'


## Build

Intalando Kind e Kubectl:

```bash 
# kind 
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.32.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# kubectl 
sudo apt update
sudo apt install kubectl

# verify 
kind version && kubectl version --client 
```

Criando um cluster com o kind:

```bash 
kubectl create namespace airflow
kind create cluster --name lab 
kubectl cluster-info --context kind-lab 
kubectl get nodes 
```

Baixando imagem Airflow com Helm:

```bash 
helm repo add apache-airflow https://airflow.apache.org 
helm repo update 
helm search repo airflow 
```

Intalando imagem no contexto 'airflow':

```bash 
helm install airflow apache-airflow/airflow \
    --namespace airflow \
    --set executor=CeleryExecutor \
    --timeout 10m
```

Configurando porta do pod Airflow:

```bash 
kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow 
```

Undoing all:

```bash 
helm uninstall airflow -n airflow 
kubectl delete namespace airflow 
kind delete cluster --name lab
```

## Help

Comandos comuns do kubectl:

```{bash}
# list running pods
kubectl get pods                    

# list deploing pods
kubectl get deployments

# debug why something's broken
kubectl describe pod <name>         

# like `docker logs`
kubectl logs <pod-name>             

# reconcile to this desired state
kubectl apply -f deployment.yaml    

# shell into a running container
kubectl exec -it <pod-name> -- bash 

# Checando pods de um contexto
kubectl get pods -n airflow
```

Comandos comuns do helm:

```{bash}
# scaffold a new chart
helm create my-chart              

helm install my-release ./my-chart --values prod-values.yaml

helm upgrade my-release ./my-chart --set image.tag=v2

# like a terraform state rollback, but easier
helm rollback my-release 1        

helm uninstall my-release
```
