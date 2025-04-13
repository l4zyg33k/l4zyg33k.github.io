# 클램쉘 모드 사용하기

## 문제
리눅스 부팅을 할 때 절전 모드로 진행이 된다.

## 해결
systemd-logind 에서 랩탑이 닫히면 절전 모드로 진행 시키기 때문에 외부 전원이 연결되면 무시하도록 설정 한다.

/etc/systemd/logind.conf
```properties
HandleLidSwitchExternalPower=ignore
```