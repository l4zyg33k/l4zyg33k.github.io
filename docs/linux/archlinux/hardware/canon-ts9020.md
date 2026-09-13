---
tags: [platform/linux/arch-linux, domain/hardware/printing, task/install, component/cups]
doc_type: how-to
---

# Canon TS9020 설정 치트시트

> 환경: Arch Linux, CUPS, Avahi

## 1. 패키지 설치

```shell
sudo pacman -Syu cups avahi sane
yay -Syu cnijfilter2 scangearmp2-sane-git
```

## 2. 설정 파일

`/etc/nsswitch.conf`

```properties
hosts: mymachines mdns_minimal [NOTFOUND=return] resolve [!UNAVAIL=return] files myhostname dns
```

## 3. 서비스 실행 및 확인

```shell
sudo systemctl enable --now cups.service avahi-daemon.service
lpstat -r
scanimage -L
```

## 4. 트러블슈팅

!!! warning
    네트워크 프린터를 찾지 못하면 같은 네트워크에 연결되어 있는지, 그리고 방화벽에서 mDNS(UDP 5353)를 차단하지 않는지 확인합니다.
