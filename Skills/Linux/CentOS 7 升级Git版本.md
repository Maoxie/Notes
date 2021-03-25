## 通过 IUS 源安装

1、确认你的当前 Git 版本

在终端输入：

```bash
git --version
```

2、卸载旧版本

```bash
sudo yum remove git*
```

3、添加 IUS CentOS 7 repo 并安装Git

```bash
sudo yum -y install  https://centos7.iuscommunity.org/ius-release.rpm
sudo yum -y install  git2u-all
```

4、检查当前 Git 版本

```bash
git --version
```

