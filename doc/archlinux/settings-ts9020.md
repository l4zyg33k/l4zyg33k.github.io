# 캐논 TS9020 잉크젯 프린터 설정하기

## 프린터
### sane 데몬 설지
```shell
pacin cups
sudo systemctl enable cups.service
sudo systemctl start cups.service
```

### IPPS 프로토콜 사용
/etc/nsswitch.conf
```properties
hosts: mymachines mdns_minimal [NOTFOUND=return] resolve [!UNAVAIL=return] files myhostname dns
```
```shell
sudo systemctl enable avahi-daemon.service
sudo systemctl start avahi-daemon.service
```

### 드라이버 설치
```shell
yay -Syu cnijfilter2
```

## 스캐너
### sane 설치
```shell
pacin sane
```

### scangearmp2-sane-git 설치
```shell
yay -Syu scangearmp2-sane-git
```