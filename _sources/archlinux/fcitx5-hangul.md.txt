# fcitx5 한글 입력

## fcitx5 설치
fcitx5 패키지를 설치 합니다.
```shell
pacman -Syu fcitx5-im fcitx5-hangul
```

## 환경 변수 설정
~/.config/environment.d 폴더에 envvars.conf 파일에 입력기 관련 환경 변수를 설정 합니다.
```
XMODIFIERS=@im=fcitx
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
```