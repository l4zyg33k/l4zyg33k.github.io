# Rootless Podman으로 kind 사용하기

kubernetes 개발 환경을 구성하기 위해 kind를 사용한 기록 입니다.

## Podman 설치하기
[Podman](https://wiki.archlinux.org/title/Podman) 문서를 참고 합니다.
```shell
sudo pacman -S podman podman-docker cni-plugins aardvark-dns

```

## Podman Rootless 설정
[Rootless](https://kind.sigs.k8s.io/docs/user/rootless/) 문서를 참고 합니다.
/etc/systemd/system/user@.service.d/delegate.conf 파일을 생성하고 아래 내용을 넣습니다.
```
[Service]
Delegate=yes
```
systemd를 리로드 합니다. 그리고, 사용자 계정으로 podman 소켓을 활성화 합니다.
```shell
sudo systemctl daemon-reload
systemctl --user start podman.socket

```