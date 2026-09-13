---
tags: [platform/linux/arch-linux, domain/system/boot, task/configure, component/plymouth]
doc_type: how-to
---

# Arch Linux 개인화 치트시트

> 환경: Arch Linux, systemd-boot, Plymouth

## 1. 패키지 설치

```shell
sudo pacman -Syu plymouth
```

## 2. 설정 파일

`/etc/plymouth/plymouth.conf`

```ini
[Daemon]
Theme=spinfinity
DeviceScale=2.0
```

`/boot/loader/entries/arch.conf`의 `options` 줄에 `quiet splash`를 추가합니다.

```properties
options root=UUID=<root-partition-uuid> rw quiet splash
```

## 3. 서비스 실행 및 확인

```shell
sudo mkinitcpio -P
sudo reboot
```

## 4. 트러블슈팅

!!! warning
    부팅 화면이 나타나지 않으면 Plymouth 훅이 initramfs 설정에 포함되었는지 확인한 뒤 `mkinitcpio -P`를 다시 실행합니다.
