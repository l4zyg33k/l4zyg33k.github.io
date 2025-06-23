# 트러블 슈팅

## 클램쉘 모드 사용하기
리눅스 부팅을 할 때 절전 모드로 진행이 된다.

### 해결
systemd-logind 에서 랩탑이 닫히면 절전 모드로 진행 시키기 때문에 외부 전원이 연결되면 무시하도록 설정 한다.

/etc/systemd/logind.conf
```properties
HandleLidSwitchExternalPower=ignore
```

## 그놈 키링 입력
매번 그놈 키링 패스워드를 입력해야 한다.

### 해결
seahorse 를 설치하고 login 키링에 대해 패스워드를 빈 값으로 변경 한다.

```shell
pacman -Syu seahorse
```