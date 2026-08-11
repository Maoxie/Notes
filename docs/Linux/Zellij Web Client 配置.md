---
type: note
aliases: ["Zellij 浏览器访问", "Zellij Web Client"]
created: 2026-07-27T23:52:00.000+0800
modified: 2026-07-27T23:52:00.000+0800
tags:
  - Linux
  - Zellij
---

# Zellij Web Client 配置

Zellij 0.43.0 起内置 Web Client，可以在浏览器中创建、连接和恢复 Zellij session。本文介绍如何配置登录 Token、局域网访问和 HTTPS。

> [!warning]
> Web Client 相当于向访问者开放当前用户的终端。不要将服务直接暴露到公网；如需公网访问，应在前面部署带限流和访问控制的反向代理，或仅通过 VPN 访问。

## 1. 前置检查

确认 Zellij 版本不低于 0.43.0：

```bash
zellij --version
```

Zellij 的默认配置文件是 `~/.config/zellij/config.kdl`。如果文件不存在，先创建配置目录并生成默认配置：

```bash
mkdir -p ~/.config/zellij
zellij setup --dump-config > ~/.config/zellij/config.kdl
```

## 2. 本机测试

启动 Web Server：

```bash
zellij web
```

默认监听 `http://127.0.0.1:8082`。浏览器打开该地址后，可以创建新 session、连接已有 session，或恢复已退出的 session。

也可以直接使用 session 名称访问：

```text
http://127.0.0.1:8082/my-session
```

如果 `my-session` 不存在，Zellij 会创建它；如果已经存在，则会直接连接。

## 3. 配置登录 Token

创建具有完整操作权限的 Token：

```bash
zellij web --create-token
```

Token 只会显示一次，应立即保存到密码管理器。Zellij 在本地数据库中只保存 Token 的哈希，因此丢失后无法找回，只能撤销并重新创建。

如只希望他人观看 session，不允许输入命令，可以创建只读 Token：

```bash
zellij web --create-read-only-token
```

也可以指定一个便于识别的名称：

```bash
zellij web --create-read-only-token --token-name "observer-token"
```

在 Zellij 中按 `Ctrl o`，再按 `s`，可打开 Share 插件并创建、查看或撤销 Token。撤销登录 Token 后，由它生成的浏览器会话凭据也会同时失效。

> [!tip]
> 浏览器快捷键容易与 Zellij 快捷键冲突，Web Client 推荐使用 unlock-first 键位预设。

## 4. 配置局域网 HTTPS

Zellij 监听非 `127.0.0.1` 地址时强制要求 HTTPS。下面使用 [mkcert](https://github.com/FiloSottile/mkcert) 创建由本地 CA 签发的证书。

### 4.1 安装 mkcert

Ubuntu/Debian：

```bash
sudo apt install libnss3-tools
sudo apt install mkcert
```

macOS：

```bash
brew install mkcert
```

如果发行版仓库中没有 `mkcert`，请参考 mkcert 项目的安装说明。

### 4.2 生成证书

先查询服务器的局域网 IP，例如 `192.168.1.105`：

```bash
hostname -I
```

安装本地 CA，然后为实际访问时使用的主机名和 IP 生成证书：

```bash
mkcert -install
mkdir -p ~/.certs/zellij
cd ~/.certs/zellij
mkcert localhost 127.0.0.1 192.168.1.105 zellij.home.arpa
```

命令会生成证书和私钥，例如：

```text
localhost+3.pem
localhost+3-key.pem
```

限制私钥权限：

```bash
chmod 600 ~/.certs/zellij/*-key.pem
```

证书的 SAN 必须包含浏览器地址栏中使用的 IP 或域名。服务器 IP 改变后，需要重新签发证书；因此建议通过 DHCP 静态租约固定 IP，或配置稳定的局域网 DNS 名称。

### 4.3 配置 Zellij

编辑 `~/.config/zellij/config.kdl`，加入以下配置，并替换用户名、证书文件名：

```kdl
web_server true
web_server_ip "0.0.0.0"
web_server_port 8082
web_server_cert "/home/your-user/.certs/zellij/localhost+3.pem"
web_server_key "/home/your-user/.certs/zellij/localhost+3-key.pem"
enforce_https_on_localhost true
```

配置说明：

- `web_server true`：启动 Zellij 时自动启动 Web Server。
- `web_server_ip "0.0.0.0"`：监听所有 IPv4 网卡，使局域网设备可以访问。
- `web_server_port 8082`：监听端口；使用大于 1024 的端口无需 root 权限。
- `web_server_cert`、`web_server_key`：TLS 证书和私钥的绝对路径。
- `enforce_https_on_localhost true`：本机访问也强制使用 HTTPS。

重启 Zellij Web Server，然后检查状态：

```bash
zellij web --status
```

局域网设备通过以下地址访问：

```text
https://192.168.1.105:8082
https://zellij.home.arpa:8082
```

### 4.4 信任本地 CA

`mkcert -install` 只会让生成证书的机器信任该 CA。其他电脑或移动设备仍会显示证书警告，需要将 mkcert 的根证书安全地导入客户端的系统信任存储。

查看根 CA 所在目录：

```bash
mkcert -CAROOT
```

将该目录中的 `rootCA.pem` 安全地复制到客户端并设置为受信任的根证书。不要复制或泄露 `rootCA-key.pem`，它可以签发任意受信任证书。

> [!note]
> 在客户端导入根 CA 只能解决证书信任问题。访问地址仍必须与证书中的 IP 或域名一致。

### 4.5 放行防火墙

如果服务器启用了 UFW，仅允许当前局域网网段访问 8082 端口：

```bash
sudo ufw allow from 192.168.1.0/24 to any port 8082 proto tcp
sudo ufw status
```

不要使用不限制来源的 `ufw allow 8082`，除非主机只连接可信网络。

## 5. 使用和维护

直接打开指定 session：

```text
https://192.168.1.105:8082/my-session
```

检查服务状态：

```bash
zellij web --status
```

如果局域网无法访问，依次检查：

1. `zellij web --status` 是否显示服务在线。
2. 配置是否监听 `0.0.0.0:8082`。
3. 证书和私钥路径是否正确，运行 Zellij 的用户是否有读取权限。
4. 防火墙是否允许客户端所在网段访问 TCP 8082。
5. 浏览器地址是否与证书中的 IP 或域名一致。
6. 客户端是否已经信任 mkcert 根 CA。

## 参考资料

- [Zellij Web Client 文档](https://zellij.dev/documentation/web-client)
- [Zellij Web Client 教程](https://zellij.dev/tutorials/web-client/)
- [mkcert](https://github.com/FiloSottile/mkcert)
