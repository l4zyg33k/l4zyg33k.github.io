# 나만의 아치리눅스 취향

## 부팅 스플래시 설정

### Plymouth 설치
[Plymouth](https://wiki.archlinux.org/title/Plymouth) 문서를 참고 합니다.
```shell
sudo pacman -S plymouth

```

### Plymouth 테마 설정
/etc/plymouth/plymouth.conf 파일에 테마를 설정 합니다.
```
[Daemon]
Theme=spinfinity
DeviceScale=2.0
```
/boot/loader/entries/arch.conf 파일에 quiet splash를 추가 합니다.
```
title Arch Linux
linux /vmlinuz-linux
initrd /intel-ucode.img
initrd /initramfs-linux.img
options root=/dev/nvme0n1p3 rw quiet splash lsm=apparmor ideapad_laptop.allow_v4_dytc=1 i8042.direct i8042.dumbkbd 
```