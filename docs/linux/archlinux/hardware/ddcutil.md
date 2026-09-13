---
tags: [platform/linux/arch-linux, domain/hardware/display, task/operate, component/ddcutil]
doc_type: how-to
---

# ddcutil 모니터 밝기 제어 치트시트

> 환경: Arch Linux, DDC/CI 지원 외부 모니터

## 1. 패키지 설치

```shell
sudo pacman -Syu ddcutil
```

## 2. 설정 파일

`/etc/modules-load.d/i2c-dev.conf`

```properties
i2c_dev
```

`/etc/systemd/system/ddcutil.service`

```ini
[Unit]
Description=Set external monitor brightness
After=display-manager.service graphical.target

[Service]
Type=oneshot
ExecStart=/usr/local/bin/ddcutil-brightness.sh

[Install]
WantedBy=graphical.target
```

## 3. 서비스 실행 및 확인

```shell
sudo modprobe i2c_dev
ddcutil detect
ddcutil setvcp 10 100
sudo systemctl enable --now ddcutil.service
```

## 4. 트러블슈팅

!!! warning
    `ddcutil detect`에 모니터가 보이지 않으면 케이블·도크가 DDC/CI를 전달하는지와 모니터 OSD에서 DDC/CI가 활성화되었는지 확인합니다.
