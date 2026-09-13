---
tags: [platform/linux/arch-linux, domain/security/authentication, task/configure, component/howdy]
doc_type: how-to
---

# Howdy 얼굴 인증 치트시트

> 환경: Arch Linux, Howdy, systemd

## 1. 패키지 설치

```shell
yay -Syu howdy
```

## 2. 설정 파일

`/usr/lib/security/howdy/config.ini`

```ini
ignore_closed_lid = false
device_path = /dev/videoX
```

`/etc/pam.d/sudo`의 인증 규칙 상단에 Howdy PAM 모듈을 추가합니다.

```properties
auth sufficient pam_python.so /lib/security/howdy/pam.py
```

## 3. 서비스 실행 및 확인

```shell
sudo howdy add
sudo howdy test
```

## 4. 트러블슈팅

!!! warning
    PAM 설정을 잘못 바꾸면 로그인할 수 없습니다. 변경 전 TTY 로그인 또는 다른 관리자 세션을 열어 두고, 인증 실패 시 추가한 PAM 행을 제거합니다.
