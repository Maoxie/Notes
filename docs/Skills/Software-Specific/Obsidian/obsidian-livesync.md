# obsidian-livesync

> [obsidian-livesync/docs/setup_own_server.md](https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/setup_own_server.md#2-run-couchdb-initsh-for-initialise)

## 0. 安装依赖

> [安装Docker并使用_云服务器 ECS(ECS)-阿里云帮助中心](https://help.aliyun.com/zh/ecs/use-cases/deploy-and-use-docker-on-alibaba-cloud-linux-2-instances?spm=5176.22414175.sslink.1.775b33actyjx4g)

```bash
yum remove docker \
    docker-client \
    docker-client-latest \
    docker-common \
    docker-latest \
    docker-latest-logrotate \
    docker-logrotate \
    docker-engine
yum install -y yum-utils \
  device-mapper-persistent-data \
  lvm2
yum-config-manager \
    --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum install docker-ce docker-ce-cli containerd.io
sudo systemctl start docker
```

## 1. 安装 CouchDB 服务端

使用该工程的 `docker-compose.yml` 文件，启动 CouchDB 服务端。

> [vrtmrz/self-hosted-livesync-server](https://github.com/vrtmrz/self-hosted-livesync-server/tree/main)

```bash
git clone --depth=1 https://github.com/vrtmrz/self-hosted-livesync-server.git
```

修改 `docker-compose.yml` 和 `config/init.ini` 文件

配置环境变量

```properties
COUCHDB_SERVER=http://localhost:5984
COUCHDB_USER=admin
COUCHDB_PW=password
```

## 2. 初始化

```bash
# Prepare environment variables.
export hostname=localhost:5984
export username=admin
export password=password

curl -s https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/utils/couchdb/couchdb-init.sh | bash
```

## 3. 暴露服务端口

## 4. 配置客户端

```bash
# Prepare environment variables.
export hostname=localhost:5984
export username=admin
export password=password

curl -s https://raw.githubusercontent.com/vrtmrz/obsidian-livesync/main/utils/couchdb/couchdb-init.sh | bash
```
