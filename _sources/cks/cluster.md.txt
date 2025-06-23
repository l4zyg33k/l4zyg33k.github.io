# 멀티패스로 CKS 실습 환경 만들기
## 마스터 노드 생성
```shell
multipass set local.driver=libvirt
sudo systemctl restart multipassd.service
multipass launch -c 2 -d 50G -m 4G -n cks-master focal
multipass shell cks-master
sudo -i
bash <(curl -s https://raw.githubusercontent.com/killer-sh/cks-course-environment/master/cluster-setup/latest/install_master.sh)
```
## 워커 노드 생성
```shell
multipass launch -c 2 -d 50G -m 4G -n cks-worker focal
multipass shell cks-worker
sudo -i
bash <(curl -s https://raw.githubusercontent.com/killer-sh/cks-course-environment/master/cluster-setup/latest/install_worker.sh)
```