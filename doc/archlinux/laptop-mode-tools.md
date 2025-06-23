# Laptop mode tools 사용하기

## acpid 서비스 설치
```shell
pacin acpid
systemctl enable acpid.service
systemctl start acpid.service
```

## laptop-mode-tooles 설치
```shell
yay -Syu laptop-mode-toole
systemctl enable laptop-mode.service
systemctl start laptop-mode.service
```