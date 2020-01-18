## 问题原因：

FTP服务端配置上要求客户段复用session，即控制session和数据传输session必须相同。

## 解决方案：

python 3.6即以上版本，可以通过以下代码解决（继承 ftplib.FTP_TLS 类，重载 ntransfercmd 方法）

```python
class ReusedSslSocket(SSLSocket):
    def unwrap(self):
        pass


class MyFTP_TLS(ftplib.FTP_TLS):
    """Explicit FTPS, with shared TLS session"""
    def ntransfercmd(self, cmd, rest=None):
        conn, size = ftplib.FTP.ntransfercmd(self, cmd, rest)
        if self._prot_p:
            conn = self.context.wrap_socket(conn,
                                            server_hostname=self.host,
                                            session=self.sock.session)  # reuses TLS session            
            conn.__class__ = ReusedSslSocket  # we should not close reused ssl socket when file transfers finish
        return conn, size
```

