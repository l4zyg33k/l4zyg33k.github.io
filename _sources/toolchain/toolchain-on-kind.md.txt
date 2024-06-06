# 개발을 위한 툴체인 구성

kompose를 이용하여 docker-compose.yaml 파일을 이용하여 쿠버네티스 자원을 만들어 사용합니다.

## 클러스터 생성

### kind 클러스터
gitea의 호스트를 tls를 사용하지 않도록 설정 합니다. 그리고, 호스트의 80, 443 포트를 매핑 합니다.
```yaml
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
containerdConfigPatches:
- |-
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors."gitea.192.168.1.129.nip.io"]
    endpoint = ["http://gitea.192.168.1.129.nip.io"]
  [plugins."io.containerd.grpc.v1.cri".registry.configs]
    [plugins."io.containerd.grpc.v1.cri".registry.configs."gitea.192.168.1.129.nip.io".tls]
      insecure_skip_verify = true
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: 80
    protocol: TCP
  - containerPort: 443
    hostPort: 443
    protocol: TCP 
```
새로운 클러스터를 생성 합니다.
```shell
kind create cluster -f cluster.yaml --name kind-1
```

### sysctl.d 설정
/etc/sysctl.d/99-sysctl.conf 를 생성 합니다.
```properties
fs.inotify.max_user_watches = 524288
fs.inotify.max_user_instances = 512
net.ipv4.ip_unprivileged_port_start = 80 
```

## 인그레스
```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml
kubectl patch cm -n ingress-nginx ingress-nginx-controller --type json --patch '[{ "op": "add", "path": "/data/worker-processes", "value": "1" }]'
```

## 도커 컴포즈
```yaml
version: '3.9'

services:

  postgres:
    image: postgres
    restart: always
    volumes:
      - pg-data:/var/lib/postgresql/data
    environment:
      - POSTGRES_PASSWORD=postgres
      - TZ=Asia/Seoul
    ports:
      - 5432
    labels:
      kompose.service.type: headless
      kompose.controller.type: statefulset     
      kompose.volume.size: 1Gi
      kompose.volume.storage-class-name: standard
      kompose.volume.type: persistentVolumeClaim

  adminer:
    image: adminer
    restart: always
    depends_on:
      - postgres
    ports:
      - 8080
    labels:
      kompose.service.expose: "adminer.192.168.1.129.nip.io"
      kompose.service.expose.ingress-class-name: nginx

  redmine:
    image: redmine
    restart: always
    depends_on:
      - postgres
    volumes:
      - rm-files:/usr/src/redmine/files
      - rm-plugins:/usr/src/redmine/plugins
      - rm-themes:/usr/src/redmine/public/themes
    ports:
      - 3000
    environment:
      - REDMINE_DB_POSTGRES=postgres
      - REDMINE_DB_USERNAME=redmine
      - REDMINE_DB_PASSWORD=redmine
      - REDMINE_DB_DATABASE=redmine
      - REDMINE_PLUGINS_MIGRATE=true
      - TZ=Asia/Seoul
    labels:
      kompose.service.expose: "redmine.192.168.1.129.nip.io"
      kompose.service.expose.ingress-class-name: nginx
      kompose.volume.size: 1Gi
      kompose.volume.storage-class-name: standard
      kompose.volume.type: persistentVolumeClaim

  gitea:
    image: gitea/gitea
    environment:
      - USER_UID=1000
      - USER_GID=1000
      - GITEA__database__DB_TYPE=postgres
      - GITEA__database__HOST=postgres:5432
      - GITEA__database__NAME=gitea
      - GITEA__database__USER=gitea
      - GITEA__database__PASSWD=gitea
      - TZ=Asia/Seoul
    restart: always
    volumes:
      - gt-data:/data
    ports:
      - 3000
      - 22
    depends_on:
      - postgres
    labels:
      kompose.service.expose: "gitea.192.168.1.129.nip.io"
      kompose.service.expose.ingress-class-name: nginx
      kompose.volume.size: 1Gi
      kompose.volume.storage-class-name: standard
      kompose.volume.type: persistentVolumeClaim

  jenkins:
    image: jenkins/jenkins
    environment:
      - TZ=Asia/Seoul
    ports:
      - 8080
      - 50000
    volumes:
      - jk-home:/var/jenkins_home
    labels:
      kompose.service.expose: "jenkins.192.168.1.129.nip.io"
      kompose.service.expose.ingress-class-name: nginx
      kompose.volume.size: 1Gi
      kompose.volume.storage-class-name: standard
      kompose.volume.type: persistentVolumeClaim

volumes:

  pg-data:
  rm-files:
  rm-plugins:
  rm-themes:
  gt-data:
  jk-home:
```

### kompose 변환
```shell
kompose convert -f docker-compose.yaml
```

## 데이터베이스

### PostgreSQL 설치
```shell
kubectl apply -f pg-data-persistentvolumeclaim.yaml -f postgres-deployment.yaml -f postgres-deployment.yaml -f postgres-service.yaml
```

### 레드마인 데이터베이스 생성
```sql
CREATE USER redmine password 'redmine';
CREATE DATABASE redmine WITH owner = redmine lc_collate = 'C' template = template0; 
```

### Gitea 데이터베이스 생성
```sql
CREATE USER gitea password 'gitea';
CREATE DATABASE gitea WITH owner = gitea lc_collate = 'C' template = template0; 
```

### Adminer 설치
```shell
kubectl apply -f adminer-deployment.yaml -f adminer-service.yaml -f adminer-ingress.yaml
```

## 깃 리파지토리

### Gitea 설치
```shell
kubectl apply -f gt-data-persistentvolumeclaim.yaml -f gitea-deployment.yaml -f gitea-service.yaml -f gitea-ingress.yaml
```

## 프라이빗 리파지토리 설정
/etc/containers/registries.conf.d 에 nip.io.conf로 추가 합니다.
```properties
[[registry]]
prefix = '*.nip.io'
insecure = true
```

```shell
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```
