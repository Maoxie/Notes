**创建配置文件，定义pip安装源**

**Linux方法：**

Linux：

$HOME/.config/pip/pip.conf 

或者 

$HOME/.pip/pip.conf（推荐）

### 创建~/.pip目录 ，新建 ~/.pip/pip.conf文件，内容如下：

```ini
[global]
timeout =6000
index-url =http://pypi.douban.com/simple/
[install]
use-mirrors =true 
mirrors =http://pypi.douban.com/simple/ 
trusted-host =pypi.douban.com
```

也可以简写为：

```ini
[global]
index-url =http://pypi.douban.com/simple/
[install]
trusted-host =pypi.douban.com
```



