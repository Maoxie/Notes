

### 1. 备份系统的repo文件
```bash
cd /etc/yum.repos.d/
mv CentOS-Base.repo CentOS-Base.repo.bak
```

### 2. 下载repo文件（网易源）
```bash
wget -O CentOS-Base.repo wget http://mirrors.163.com/.help/CentOS7-Base-163.repo
```

### 3. 清理缓冲，重建缓存，更新
```bash
yum clean all
yum makecache
yum update
```