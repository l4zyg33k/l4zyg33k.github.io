---
tags: [platform/linux/arch-linux, domain/ai/inference, task/install, component/openvino-model-server]
doc_type: how-to
---

# OpenVINO Model Server 치트시트

> 환경: Arch Linux, Podman, Intel GPU/NPU

## 1. 패키지 설치

```shell
sudo pacman -Syu intel-compute-runtime podman
yay -Syu intel-npu-driver
```

## 2. 설정 파일

`./models/config_all.json`

```json
{
  "model_config_list": []
}
```

## 3. 서비스 실행 및 확인

```shell
podman run -d --name ovms --rm \
  --device /dev/accel --group-add keep-groups \
  -p 8000:8000 -v "$PWD/models:/workspace/models:Z" \
  openvino/model_server:latest \
  --rest_port 8000 --config_path /workspace/models/config_all.json
curl http://localhost:8000/v1/config
```

## 4. 트러블슈팅

!!! warning
    가속기 장치 접근이 거부되면 `/dev/accel`과 `/dev/dri`의 권한 및 컨테이너 실행 사용자의 그룹을 확인합니다.
