pip豆瓣源

```bash
pip -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
```

全局配置pip源

```ini
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```

```bash
# 使用python2
py -2
```



pip源配置文件可以放置的位置：

```bash
Linux/Unix:

/etc/pip.con

~/.pip/pip.conf （每一个我都找了都没有，所以我是在这个文件夹中创建的pip.conf文件）

~/.config/pip/pip.conf
```

Mac OSX:

```bash
~/Library/Application Support/pip/pip.conf

~/.pip/pip.conf

/Library/Application Support/pip/pip.conf
```

Windows:

```bash
%APPDATA%\pip\pip.ini

%HOME%\pip\pip.ini

C:\Documents and Settings\All Users\Application Data\PyPA\pip\pip.conf (Windows XP)

C:\ProgramData\PyPA\pip\pip.conf (Windows 7及以后)
```