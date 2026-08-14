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
kind create cluster --name lab 
kubectl cluster-info --context kind-lab 
kubectl get nodes 
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
