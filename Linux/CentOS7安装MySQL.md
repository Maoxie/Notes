# CentOS 7 安装MySQL

翻译自官方安装指南

> A Quick Guide to Using the MySQL Yum Repository[https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/](https://dev.mysql.com/doc/mysql-yum-repo-quick-guide/en/)

## 1. 添加MySQL Yum Repository

1. 到MySQL Yum repository 的下载页面[https://dev.mysql.com/downloads/repo/yum/](https://dev.mysql.com/downloads/repo/yum/)
2. 选择并下载对应平台的发行包(release package)
3. 执行以下命令，安装下载的发行包。将其中的*platform-and-version-specific-package-name*替换为包名:

```bash
shell> sudo rpm -Uvh platform-and-version-specific-package-name.rpm
```

> 注意
>
> 一旦安装了发行包，任何通过`yum update`命令进行的全系统的升级（update）操作都会自动升级（upgrade）系统上的MySQL包，并且如果yum在MySQL Yum repository中发现了原生第三方包的替代，会自动替换掉它们。
>
> Once the release package is installed on your system, any system-wide update by the **yum update** command (or **dnf upgrade** for dnf-enabled systems) will automatically upgrade MySQL packages on your system and also replace any native third-party packages, if Yum finds replacements for them in the MySQL Yum repository.

## 2. 选择发行版本

默认安装MySQL的最新公开发行版。如果不需要选择，可以跳过这一步。

在MySQL Yum repository 中，MySQL Community Server的不同系列存放于不同的子仓库中。默认enable的子仓库为当前最新的公开发行版。用以下命令可以查看有哪些子仓库。

```bash
shell> yum repolist all | grep mysql
```

想要选择子仓库，可以用`yum-config-manager`命令，先disable默认子仓库，然后enable想要使用的子仓库。

```bash
shell> sudo yum-config-manager --disable mysql80-community
shell> sudo yum-config-manager --enable mysql57-community
```

此外，也可以通过编辑`/etc/yum.repos.d/mysql-community.repo`文件来设置。

```ini
[mysql80-community]
name=MySQL 8.0 Community Server
baseurl=http://repo.mysql.com/yum/mysql-8.0-community/el/6/$basearch/
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-mysql
```

如上，修改对应子仓库的enabled值为0、1即可将其禁用、启用。

然后输入以下命令确认修改结果

```bash
shell> yum repolist enabled | grep mysql
```

## 3. 安装MySQL

输入以下命令，将会安装MySQL及其依赖包。

```bash
shell> sudo yum install mysql-community-server
```

## 4. 启动MySQL服务

通过以下命令启动MySQL服务：

```bash
shell> sudo service mysqld start
```

对于基于EL7的平台，推荐使用以下命令启动：（CentOS7看这里）

```bash
shell> sudo systemctl start mysqld.service
```

可使用以下命令检查MySQL服务的状态

```bash
shell> sudo service mysqld status
```

对于基于EL7的平台，推荐使用以下命令检查MySQL服务的状态：（CentOS7看这里）

```bash
shell> sudo systemctl status mysqld.service
```

### MySQL服务初始化过程：

在服务初次启动时，服务端的数据目录为空，发生以下事件：

- 服务初始化。

- 在数据目录生成SSL证书(certificate )文件和密钥(key)文件。

- 安装和启用[validate_password 插件](https://dev.mysql.com/doc/refman/8.0/en/validate-password.html) 。

- 创建超级用户账号`'root'@'localhost'`，生成超级用户的密码并保存在error log文件中。通过以下命令可查看：

  ```bash
  shell> sudo grep 'temporary password' /var/log/mysqld.log
  ```

  尽快用生成的临时root账号的密码登陆，然后设置自定的超级用户密码：

  ```bash
  shell> mysql -uroot -p
  ```
  
  ```mysql
  mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'MyNewPass4!';
  ```
  
  
  
  
