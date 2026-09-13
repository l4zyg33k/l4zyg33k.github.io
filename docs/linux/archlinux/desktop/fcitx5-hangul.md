---
tags: [platform/linux/arch-linux, domain/desktop/input, task/configure, component/fcitx5]
doc_type: how-to
---

# fcitx5 한글 입력 치트시트

> 환경: Arch Linux, systemd 사용자 세션

## 1. 패키지 설치

```shell
sudo pacman -Syu fcitx5-im fcitx5-hangul
```

## 2. 설정 파일

`~/.config/environment.d/fcitx5.conf`

```properties
XMODIFIERS=@im=fcitx
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
```

## 3. 서비스 실행 및 확인

```shell
systemctl --user import-environment
fcitx5-diagnose
```

로그아웃 후 다시 로그인하여 환경 변수를 적용합니다.

## 4. 트러블슈팅

!!! warning
    Wayland 세션에서 입력기가 보이지 않으면 데스크톱 환경의 자동 시작 항목에 `fcitx5 -d`를 추가하고 다시 로그인합니다.
