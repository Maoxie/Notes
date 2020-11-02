# 创建配置文件，定义pip安装源

## Linux 方法

```$HOME/.config/pip/pip.conf ```

或者 

```$HOME/.pip/pip.conf```（推荐）

**创建~/.pip目录 ，新建 ~/.pip/pip.conf文件，内容如下：**

```ini
[global]
index-url = http://pypi.douban.com/simple/
trusted-host = pypi.douban.com
[install]
use-mirrors = true
mirrors = http://pypi.douban.com/simple/
trusted-host = pypi.douban.com
```

也可以简写为：

```ini
[global]
index-url = http://pypi.douban.com/simple/
[install]
trusted-host = pypi.douban.com
```

另外, 使用setup.py安装依赖库, 还是会从默认的http://pypi.python.org下载, 解决方案如下:

编辑 ~/.pydistutils.cfg 文件，内容如下:

```ini
[easy_install]
index_url = https://pypi.douban.com/simple
```

## Windows 10 方法

新建 %HOME%\pip\pip.ini 文件，内容同上

