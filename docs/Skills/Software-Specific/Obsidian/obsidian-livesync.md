# obsidian-livesync

> [obsidian-livesync/docs/setup_own_server.md](https://github.com/vrtmrz/obsidian-livesync/blob/main/docs/setup_own_server.md#2-run-couchdb-initsh-for-initialise)

## 1. 安装 CouchDB 服务端

使用该工程的 `docker-compose.yml` 文件，启动 CouchDB 服务端。

> [vrtmrz/self-hosted-livesync-server](https://github.com/vrtmrz/self-hosted-livesync-server/tree/main)

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
