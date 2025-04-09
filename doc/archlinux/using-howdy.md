# Howdy 로 인증하기

## 설치 하기
```shell
yay -Syu howdy
```

## 설정 하기
랩탑의 카메라는 /dev/video0 이며, 데스크탑의 카메라는 /dev/video4 로 인식 됩니다. /usr/lib/secirity/howdy/config.ini 를 변경 합니다. 클램쉘 모드를 사용하기 위해 랩탑이 닫혀도 사용 할 수 있도록 합니다. 그리고, 장치 경로로 설정 합니다.
```shell
# Disable Howdy if lid is closed
ignore_closed_lid = false

# The path of the device to capture frames from
# Should be set automatically by an installer if your distro has one
device_path = /dev/video0 
```

## 변경 하기
랩탑과 데스크탑의 전환 여부를 클램쉘 모드로 확인하여 자동화 합니다. /etc/systemd/system 에 howdy.service 로 서비스를 만듭니다.
```
Unit]                                                                                                                                                                             
Description=Howdy Service                                                                                                                                                          
After=graphical.target                                                                                                                                                             
StartLimitBurst=0                                                                                                                                                                  
                                                                                                                                                                                   
[Service]                                                                                                                                                                          
Type=oneshot                                                                                                                                                                       
ExecStart=/usr/local/bin/howdy.sh                                                                                                                                                  
Restart=on-failure                                                                                                                                                                 
RemainAfterExit=true                                                                                                                                                               
                                                                                                                                                                                   
[Install]                                                                                                                                                                          
WantedBy=graphical.target                                                                                                                                                          
~                              
```
/usr/local/bin 에 howdy.sh 를 만듭니다. howdy.service 에서 열리고 닫힘에 따라 변경해 줍니다.
```shell
#!/bin/zsh                                                                                                                                                                         
                                                                                                                                                                                   
lid_state=$(cat /proc/acpi/button/lid/LID0/state | awk '{print $2}')                                                                                                               
if [[ "$lid_state" == "open" ]]; then                                                                                                                                              
  sed -i 's/device_path = \/dev\/video4/device_path = \/dev\/video0/g' /usr/lib/security/howdy/config.ini                                                                          
elif [[ "$lid_state" == "closed" ]]; then                                                                                                                                          
  sed -i 's/device_path = \/dev\/video0/device_path = \/dev\/video4/g' /usr/lib/security/howdy/config.ini                                                                          
fi    
```

서비스를 등록 합니다.
```shell
systemctl enable ddctuil.service
```