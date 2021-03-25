# supervisor 的安装与基本命令

## 1. 安装

```bash
sudo apt install supervisor

# 为了让非root权限用户也能执行 supervisord/supervisorctl 等命令，需要修改以下路径权限
sudo chmod 777 /var/run				# supervisor.sock 文件路径
sudo chmod 777 /etc/supervisor		# 配置文件路径
sudo chmod 777 /var/log/supervisor	# 日志路径
```

启动`supervisor`服务：
```bash
# -c: 指定配置文件路径
supervisor -c /etc/supervisor/supervisor.conf
```

启动后在`/var/run`路径下生成`supervisor.sock`

### 常见错误

1. 

```
unix:///var/run/supervisord.sock refused connection?
```

说明 supervisord 未启动

2. 

```
unix:///var/run/supervisor.sock no such file
```

创建`supervisor.sock`并赋予权限

```bash
sudo touch /var/run/supervisor.sock
sudo chmod 777 /var/run/supervisor.sock
sudo systemctl restart supervisor
```

## 2. 管理命令

用`systemctl`服务管理

```bash
sudo systemctl enable supervisor	# 开启服务
sudo systemctl disable supervisor

sudo systemctl start supervisor
sudo systemctl stop supervisor
sudo systemctl restart supervisor

sudo systemctl status supervisor	# 开启服务
```

`supervisorctl`命令

```bash
supervisorctl reload	# 重新加载配置文件。每次修改配置文件后需要执行此命令

supervisorctl start task-name
supervisorctl stop task-name
supervisorctl restart all	# all表示所有项目
```

