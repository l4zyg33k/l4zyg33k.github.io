# ddcutil을 이용한 포터블 모니터 밝기 제어

## i2c-dev 모듈 로드
/etc/modules-load.d 폴더에 i2c-dev.conf 를 만들고 다음 내용을 넣어 줍니다.
```
i2c_dev
```

## ddcutil 설치
```shell
yay -Syu ddcutil
```

## 포터블 모니터 찾기
```shell
ddcutil detect

Display 2
   I2C bus:  /dev/i2c-11
   DRM connector:           card0-DP-2
   EDID synopsis:
      Mfg id:               RTK - UNK
      Model:                WCS Display
      Product code:         6683  (0x1a1b)
      Serial number:        demoset-1
      Binary serial number: 16843009 (0x01010101)
      Manufacture year:     2023,  Week: 20
   VCP version:         2.2
```

## 모니터 밝기 100으로 높이기
모델 이름과 시리얼 번호로 밝기를 조정 합니다.
```shell
ddcutil -l 'WCS Display' -n 'demoset-1' setvcp 10 100
```

## systemd 서비스 등록
display-manager.service 과 graphical.target 가 실행된 이후에 ddcutil이 실행이 되도록 합니다. /etc/systemd/system 폴더에 ddcutil.service 라는 이름으로 만듭니다.
```
[Unit]
Description=ddcutil service 
After=display-manager.service graphical.target
StartLimitBurst=0

[Service]
Type=oneshot
ExecStart=/usr/local/bin/ddcutil.sh
Restart=on-failure
RemainAfterExit=true

[Install]
WantedBy=graphical.target
```
/usr/local/bin 에 ddcutil.sh 을 만듭니다.

```shell
#!/bin/zsh

get_wcs=$(ddcutil detect | grep 'WCS Display' | wc -l)
if [[ "$get_wcs" == 1 ]]; then
  ddcutil -l 'WCS Display' -n 'demoset-1' setvcp 10 100
else
  return 0
fi

```

서비스를 등록 합니다.
```shell
systemctl enable ddctuil.service
```