## HTTPS自签名证书

### 1. 生成加密私钥

 利用openssl命令，生成2048位加密密钥。

```bash
openssl genrsa -out server.key 2048
```

在当前文件夹生成密钥文件`server.key`。

### 2. 生成证书签名请求（CSR）

```bash
openssl req -new -key server.key -out server.csr
```

此命令会要求用户输入一些信息。可根据项目需求自行修改，最终生成`server.csr`证书签名申请文件。

### 3. 成类型为X509的自签名证书

```bash
openssl x509 -req -days 36500 -in server.csr -signkey server.key -out server.crt
```

运行此命令最终生成server.crt证书文件

## Nginx配置HTTPS

主要做三件事情：放置Nginx HTTPS证书及证书秘钥，配置服务为HTTPS协议，HTTP协议自动重定向到HTTPS

### 1. 放置Nginx HTTPS证书及证书秘钥

将`server.crt`拷贝到`/etc/pki/nginx/`目录

将`server.key`文件拷贝到 `/etc/pki/nginx/private`目录

### 2. 配置服务为HTTPS协议

```nginx
    listen       443 ssl http2 default_server;
    listen       [::]:443 ssl http2 default_server;
    server_name  _;
    #root         /usr/share/nginx/html;

    ssl_certificate "/etc/pki/nginx/server.crt";                # 证书
    ssl_certificate_key "/etc/pki/nginx/private/server.key";     # 秘钥
    ssl_session_cache shared:SSL:1m;
    ssl_session_timeout  10m;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
```

### 3. 配置HTTP重定向到HTTPS

```nginx
server {
    listen      80;
    server_name   _;
    return 301 https://$host$request_uri;
}
```
