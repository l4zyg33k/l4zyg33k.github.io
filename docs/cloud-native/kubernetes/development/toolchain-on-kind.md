---
tags: [platform/cloud-native/kubernetes, domain/development/toolchain, task/install, component/kind, component/ingress-nginx]
doc_type: how-to
---

# kind 개발 툴체인 치트시트

> 환경: kind, Kubernetes, ingress-nginx, Kompose

## 1. 패키지 설치

```shell
sudo pacman -Syu kind kubectl kompose
```

## 2. 설정 파일

`cluster.yaml`

```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
    extraPortMappings:
      - containerPort: 80
        hostPort: 8080
        protocol: TCP
```

`/etc/containers/registries.conf.d/local-registry.conf`

```toml
[[registry]]
prefix = "registry.example.invalid"
location = "registry.example.invalid"
insecure = true
```

## 3. 서비스 실행 및 확인

```shell
kind create cluster --name dev --config cluster.yaml
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl get nodes
kubectl get pods -n ingress-nginx
```

## 4. 트러블슈팅

!!! warning
    실제 레지스트리 주소, 계정, 비밀번호, API 토큰은 문서나 매니페스트에 기록하지 않습니다. Kubernetes Secret 또는 CI의 비밀 변수로 주입합니다.
