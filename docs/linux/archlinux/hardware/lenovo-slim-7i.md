---
tags: [platform/linux/arch-linux, domain/hardware/laptop, task/configure, component/systemd-boot]
doc_type: how-to
---

# Lenovo Slim 7i Arch Linux 치트시트

> 환경: Arch Linux, Intel 12세대 플랫폼, systemd-boot

## 1. 패키지 설치

```shell
sudo pacman -Syu sof-firmware libva-intel-driver libva-utils intel-media-driver intel-gpu-tools
yay -S howdy ddcci-driver-linux-dkms-git
```

## 2. 설정 파일

`/boot/loader/entries/arch.conf`

```properties
options root=UUID=<root-partition-uuid> rw ideapad_laptop.allow_v4_dytc=1 i8042.direct i8042.dumbkbd
```

`/etc/mkinitcpio.conf`의 `MODULES`에 DDC/CI 모듈을 추가합니다.

```properties
MODULES=(ddcci ddcci_backlight)
```

## 3. 서비스 실행 및 확인

```shell
sudo mkinitcpio -P
vainfo
sudo reboot
```

## 4. 트러블슈팅

!!! warning
    커널 매개변수와 DKMS 모듈은 커널 업데이트 후 재확인이 필요합니다. 부팅 문제가 생기면 부트로더에서 해당 매개변수를 일시적으로 제거합니다.
