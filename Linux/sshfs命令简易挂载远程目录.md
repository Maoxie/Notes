# 使用`sshfs`命令简易挂载远程目录

## 0. 安装`sshfs`命令

Centos（需要先配置EPEL源）

```bash
yum install fuse-sshfs
```

Ubuntu

```bash
apt install sshfs
```

可选：在远程服务器上配置好SSH密钥登录，以便连接

## 1. 挂载

执行以下命令，通过ssh挂载远程目录到本地

```bash
sshfs username@hostname:/remote/dir/path /path/to/mount
```

挂载选项

```bash
# debug模式
sshfs -o debug,sshfs_debug ...
# 允许其他用户访问(需要root权限)
sudo sshfs -o allow_other ...
# 允许挂载目录非空
sshfs -o nonempty ...
# SSH连接端口
sshfs -p 222 ...
# 自定义SSH连接命令
sshfs -o ssh_command='ssh -c aes128-cbc' ...
```

## 2. 卸载

```bash
# 方法1
fusermount -u /path/to/mount
# 方法2（需要root权限）
sudo umount /path/to/mount
```

