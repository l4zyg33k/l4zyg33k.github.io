---
tags: [platform/cloud-native/kubernetes, domain/cloud-native/runtime, task/install, component/podman, component/kind]
doc_type: how-to
---

# Rootless Podman kind 치트시트

> 환경: Arch Linux, Podman rootless, kind

## 1. 패키지 설치

```shell
sudo pacman -Syu podman podman-docker cni-plugins aardvark-dns kind kubectl
```

## 2. 설정 파일

`/etc/systemd/system/user@.service.d/delegate.conf`

```ini
[Service]
Delegate=yes
```

## 3. 서비스 실행 및 확인

```shell
sudo systemctl daemon-reload
systemctl --user enable --now podman.socket
systemd-run --user --scope kind create cluster
kubectl cluster-info
```

## 4. 트러블슈팅

!!! warning
    rootless kind가 컨테이너를 시작하지 못하면 `loginctl enable-linger $USER` 및 사용자 네임스페이스 설정을 확인합니다.
