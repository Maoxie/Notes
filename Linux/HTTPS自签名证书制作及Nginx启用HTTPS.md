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