# Lenovo Slim 7i에서 아치리눅스 사용하기

[Laptop/Lenovo](https://wiki.archlinux.org/title/Laptop/Lenovo) 문서를 참고하여 intel i7 1260P의 Lenovo Slim 7i에 아치리눅스를 구성한 기록 입니다.

## 오디오 드라이버
```bash
sudo pacman -S sof-firmware 
```
## 그래픽 드라이버
```bash
sudo pacman -S libva-intel-driver libva-utils intel-media-driver intel-gpu-tools
```

### 부팅 스플래시
[Plymouth](https://wiki.archlinux.org/title/Plymouth) 문서를 참고 합니다.
```bash
sudo pacman -S plymouth

```
/boot/loader/entries/arch.conf 파일에 quiet splash를 추가한다.
```
title Arch Linux
linux /vmlinuz-linux
initrd /intel-ucode.img
initrd /initramfs-linux.img
options root=/dev/nvme0n1p3 rw quiet splash lsm=apparmor ideapad_laptop.allow_v4_dytc=1 i8042.direct
i8042.dumbkbd 
```