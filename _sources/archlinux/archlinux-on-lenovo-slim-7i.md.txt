# 레노보 슬림 7i에서 아치리눅스 사용하기

일평생 한방에 끝판왕을 가지 못하고 가난한 자의 시리즈를 거쳐가는 성향으로 맥북에어 M2를 가지지 못하고
스스로 가난한 자의 맥북에어로 칭하며 이 모델을 구입 하였습니다.
[Laptop/Lenovo](https://wiki.archlinux.org/title/Laptop/Lenovo) 문서를 참고하여 인텔
12세대 i7-1260P 프로세서의 레노보 슬림 7i에 아치리눅스를 구성한 기록 입니다. 대부분은 커널 모듈에서
제공하는 드라이버가 자동적으로 적용되며 아웃-오브-박스 처럼 바로 사용 할 수 있습니다.

## 커널 파라메터
전원 관리와 키보드에 대한 이슈 해결을 위해 커널 파라메터를 설정 합니다. 
```
ideapad_laptop.allow_v4_dytc=1 i8042.direct i8042.dumbkbd 
```

## 오디오 드라이버
돌비 아트모스가 가능한 오디오 시스템이지만 과감하게 포기 합니다. 소리가 나온다는 것으로 만족 합니다.
```shell
sudo pacman -S sof-firmware 
```

## 그래픽 드라이버
Intel® Iris® Xe Graphics로 게임 성능은 잘 모르지만 그저 하드웨어 가속만 되기를 바래봅니다.
```shell
sudo pacman -S libva-intel-driver libva-utils intel-media-driver intel-gpu-tools
```
파이어폭스에서 유튜브 컨텐츠 시청 시 하드웨어 가속기가 작동합니다.

## 적외선 카메라
윈도우의 헬로우와 같이 적외선 카메라로 사용자 인증을 할 수 있습니다. 적외선 카메라는 자동으로 인식 됩니다.

### python-dlib 준비
AUR에서는 관리가 되지 않고 있어서 [arch4edu](https://wiki.archlinux.org/title/Unofficial_user_repositories#arch4edu)
비공식 리파지토리를 추가 합니다.

#### 리파지토리 추가
/etc/pacman.conf에 아래 내용을 추가 합니다.
```
[arch4edu]
Server = https://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch
```
GPG 서버로 부터 GPG 키를 가져옵니다.
```shell
pacman-key --recv-keys 7931B6D628C8D3BA
pacman-key --finger 7931B6D628C8D3BA
pacman-key --lsign-key 7931B6D628C8D3BA
```

#### python-dlib 설치
python-dlib 패키지를 설치 합니다.
```shell
pacman -S python-dlib
```

### howdy 설치
```shell
yay -S howdy
```

### howdy 설정
[Howdy](https://wiki.archlinux.org/title/Howdy) 문서를 참고하여 /lib/security/howdy/config.ini 수정 합니다. 

#### 사용자 인식
현재 사용자를 인식 합니다.
```shell
sudo howdy add
```

#### sudo 설정
/etc/pam.d/sudo 파일 상위에 추가 합니다.
```
auth sufficient pam_python.so /lib/security/howdy/pam.py
```

#### gdm-password 설정
/etc/pam.d/gdm-password 파일 상위에 추가 합니다.
```
auth sufficient pam_unix.so try_first_pass likeauth nullok
auth sufficient pam_python.so /lib/security/howdy/pam.py
```

#### OpenCV 환경변수 설정
OpenCV의 WARN 에러가 신경 쓰이면 아래와 같이 환경 변수를 .zshenv에 추가 합니다.
```shell
export OPENCV_LOG_LEVEL=ERROR
```

## 외장 모니터 밝기
### 커널 모듈 설치
ddcci-driver-linux-dkms-git AUR 패키지를 설지 합니다.
/etc/mkinitcpio.conf 파일에서 MODULES=(ddcci ddcci_backlight)를 추가 합니다.
```
echo 'ddcci 0x37' | sudo tee /sys/bus/i2c/devices/i2c-11/new_device
ddcutil setvcp 10 50 -b 11

[  449.312601] ddcci-backlight ddcci11: registered luminance as backlight device ddcci11
[  449.906083] i2c i2c-11: new_device: Instantiated device ddcci at 0x37

```
