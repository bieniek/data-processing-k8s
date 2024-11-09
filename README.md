## Agro Workflows PDF Data processing

Below repo contains several components that enable PDF files processing

### Prerequisites

1. Install minikube (if no external k8s cluster)
2. Install kubectl
3. Install argo workflows (agro.version file required)

```kubectl apply -f "https://github.com/argoproj/argo-workflows/releases/download/` cat argo.version `/quick-start-minimal.yaml" ```

4. Install argo cli

```https://github.com/argoproj/argo-workflows/releases```

6. Run eval $(minikube docker-env) on each terminal

### Execution

1. Build docker images for preprocessing and processing components
2. Submit agro workflow (adjust parameters with PDF file)

