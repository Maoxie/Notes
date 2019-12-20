## HTTPS自签名证书

### 1. 生成加密私钥

 利用openssl命令，生成2048位加密密钥。

```bash
openssl genrsa -out server.key 2048
```

在当前文件夹生成密钥文件`server.key`。

### 2. 生成证书签名请求（CSR）



