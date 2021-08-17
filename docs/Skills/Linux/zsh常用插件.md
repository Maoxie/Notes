# ZSH 常用插件

安装 Oh-My-ZSH
```bash
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```
> https://ohmyz.sh/#install

## 1. 启用插件的方法

打开`~/.zshrc`文件找到`plugins`，然后加入要开启的插件名称。

```bash
plugins = (
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  conda-zsh-completion
)
```

执行`source ~/.zshrc`使其生效。

## 2. 推荐插件

### zsh-autosuggestions

命令自动补全

```bash
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

### zsh-syntax-highlighting

命令语法高亮插件

```bash
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```

### extract

内置插件。智能判断压缩包后缀来选择解压命令。

```bash
extract 文件名
# 或者 x 文件名
```

### themes

内置插件。快速切换主题。

```bash
theme 主题名
```

### conda-zsh-completion

conda命令补全。

**安装**：

```bash
git clone https://github.com/esc/conda-zsh-completion ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/conda-zsh-completion
```

**启用**：

修改`.zshrc`，启动插件，并重新加载`compinit`

```bash
# 将 conda-zsh-completion 加入到插件列表, 追加到最后
plugins=(git conda-zsh-completion)
# 这句放到脚本末
autoload -U compinit && compinit
```

> 附注：在zsh上自动初始化conda的配置
>
> ```bash
> conda init zsh
> ```

### autojump

实现目录间快速跳转，想去哪个目录直接 j + 目录名，不用再频繁的 cd 了！

**安装**：

```bash
git clone git://github.com/joelthelion/autojump.git
cd autojump
python ./install.py
# 卸载
# python ./uninstall.py
```

**启用**：

把以下代码加到 `~/.zshrc` 尾部

```bash
# 使用git安装的
[[ -s ~/.autojump/etc/profile.d/autojump.sh ]] && . ~/.autojump/etc/profile.d/autojump.sh
```

**使用方法**：

命令：`autojump` 或 `j`

```bash
j 目录名
```

对于权重数据库的访问

```bash
# 在数据库中添加一个目录
j -a [dir]
# 提升当前目录value数目的权重
j -i [value]
# 降低当前目录的权重
j -d [value]
# 显示数据库中的统计数据
j -s
# 清除不再需要的目录
j --purge
```

### z

内置插件。类似 autojump 。提供一个`z`命令，在常用目录之间跳转。

```bash
z 目录名
```

如果z插件历史记录太多，并且有一些不是自己想要的，可以删除

```bash
z -x 不要的路径
```

### vi-mode

内置插件。vim输入模式

### safe-paste

内置插件。当你往 zsh 粘贴脚本时，它不会被立刻运行。

### colored-man-pages

内置插件。给man添加色彩。

### sudo

内置插件。连按两下 Esc 键在命令的开头加上或去掉 sudo 关键字。

## 3. 推荐主题

**Powerlevel10k**

### (1) 安装

> https://github.com/romkatv/powerlevel10k

```bash
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
# 墙内可用gitee镜像代替
# git clone --depth=1 https://gitee.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
```

在 `~/.zshrc`中启用主题

```bash
ZSH_THEME="powerlevel10k/powerlevel10k"
```

### (2) 字体

建议使用 Nerd Fonts 系列字体，否则无法显示大部分icon。

> [ryanoasis/nerd-fonts: Iconic font aggregator, collection, & patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, & more (github.com)](https://github.com/ryanoasis/nerd-fonts)

### (3) 配置

配置向导（configuration wizard）

```bash
p10k configure
```

配置储存在`~/.p10k.zsh`

