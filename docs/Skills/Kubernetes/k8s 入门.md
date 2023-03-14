# k8s 入门

> [Getting Started | Kubernetes](https://kubernetes.io/docs/setup/)

## 1. 安装

### 1.1 minikube

> [minikube start | minikube](https://minikube.sigs.k8s.io/docs/start/)

配置minikube使用docker driver

```bash
minikube config set driver docker
```

启动一个单节点集群：

```bash
minikube start
```

管理集群

```bash
minikube pause      # pause kubernetes without impacting deployed applications
minikube unpause    # unpause a paused instance
minikube stop       # Halt the cluster
# change the default memory limit (requires a restart)
minikube config set memory 9001
# delete all of the minikube clusters
minikube delete --all
```

### 1.2 kubectl






