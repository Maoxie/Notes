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
# 指定配置文件路径
supervisor -c /etc/supervisor/supervisor.conf
```

## 2. 管理命令

服务管理

```bash
sudo systemctl enable redis
sudo systemctl start supervisor
sudo systemctl stop supervisor
sudo systemctl restart supervisor
```

`supervisorctl`命令

```bash
supervisorctl reload
supervisorctl start task-name
supervisorctl stop task-name
supervisorctl restart all	# all表示所有项目
```

