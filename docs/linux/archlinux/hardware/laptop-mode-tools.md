---
tags: [platform/linux/arch-linux, domain/hardware/power, task/operate, component/laptop-mode-tools]
doc_type: how-to
---

# Laptop Mode Tools 치트시트

> 환경: Arch Linux, systemd

## 1. 패키지 설치

```shell
sudo pacman -Syu acpid
yay -Syu laptop-mode-tools
```

## 2. 설정 파일

`/etc/laptop-mode/laptop-mode.conf`

```properties
ENABLE_LAPTOP_MODE_ON_BATTERY=1
```

## 3. 서비스 실행 및 확인

```shell
sudo systemctl enable --now acpid.service laptop-mode.service
systemctl status acpid.service laptop-mode.service
```

## 4. 트러블슈팅

!!! warning
    패키지 또는 서비스 이름은 배포판과 AUR 패키지 상태에 따라 달라질 수 있습니다. 설치 전 `pacman -Ss` 또는 AUR 패키지 정보를 확인합니다.
