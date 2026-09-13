---
tags: [platform/linux/arch-linux, domain/system/session, task/troubleshoot, component/systemd-logind]
doc_type: how-to
---

# Arch Linux 문제 해결 치트시트

> 환경: Arch Linux, GNOME, systemd-logind

## 1. 패키지 설치

```shell
sudo pacman -Syu seahorse
```

## 2. 설정 파일

`/etc/systemd/logind.conf`

```ini
[Login]
HandleLidSwitchExternalPower=ignore
```

## 3. 서비스 실행 및 확인

```shell
sudo systemctl restart systemd-logind.service
loginctl show-session "$XDG_SESSION_ID" -p State
```

GNOME 키링 암호는 Seahorse에서 `login` 키링을 선택해 변경합니다.

## 4. 트러블슈팅

!!! warning
    `systemd-logind` 재시작은 현재 세션에 영향을 줄 수 있습니다. 원격 접속 중이라면 재부팅 후 설정을 확인합니다.
