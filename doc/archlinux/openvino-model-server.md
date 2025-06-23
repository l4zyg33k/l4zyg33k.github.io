# OpenVINO 모델 서버 설치

## 인텔 드라이버 설치
```shell
pacman -Syu intel-compute-runtime
yay -Syu intel-npu-driver
```
## 모델 설치
```shell
pyenv install 3.12.11
pipenv --python 3.12.11
```
https://docs.openvino.ai/2025/model-server/ovms_demos_code_completion_vsc.html

## 모델 서버 실행 
podman run -d --rm --device /dev/accel --group-add=$(stat -c "%g" /dev/dri/render* | head -n 1) -u $(id -u):$(id -g) \
-p 8000:8000 -v $(pwd)/:/workspace/ openvino/model_server:2025.2-gpu --rest_port 8000 --config_path /workspace/models/config_all.json