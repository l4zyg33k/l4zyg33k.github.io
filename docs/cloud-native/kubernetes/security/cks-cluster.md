---
tags: [platform/cloud-native/kubernetes, domain/security/cluster, task/lab, component/multipass]
doc_type: tutorial
---

# CKS 실습 클러스터 치트시트

> 환경: Ubuntu LTS 가상 머신, Multipass, libvirt

## 1. 패키지 설치

```shell
sudo pacman -Syu multipass libvirt
sudo systemctl enable --now libvirtd.service
```

## 2. 설정 파일

`/etc/libvirt/libvirtd.conf`

```ini
unix_sock_group = "libvirt"
unix_sock_rw_perms = "0770"
```

## 3. 서비스 실행 및 확인

```shell
multipass set local.driver=libvirt
multipass launch -c 2 -d 50G -m 4G -n cks-master 24.04
multipass launch -c 2 -d 50G -m 4G -n cks-worker 24.04
multipass list
```

## 4. 트러블슈팅

!!! warning
    교육용 설치 스크립트는 버전과 출처를 검증한 뒤 사용합니다. 가상 머신의 CPU·메모리·디스크 요구량이 호스트 자원을 초과하지 않도록 합니다.
