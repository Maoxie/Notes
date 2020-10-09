> 推荐使用的主题：bureau

## 启用插件

打开`~/.zshrc`文件找到`plugins`数组，然后把插件名加入数组即算开启。

```bash
plugins = (
  git
  zsh-autosuggestions
  zsh-syntax-highlighting
  conda-zsh-completion
)
```

## 推荐插件

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

安装：

```bash
git clone https://github.com/esc/conda-zsh-completion ${ZSH_CUSTOM:=~/.oh-my-zsh/custom}/plugins/conda-zsh-completion
```

修改`.zshrc`，启动插件，并重新加载`compinit`

```bash
# 将 conda-zsh-completion 加入到插件列表, 追加到最后
plugins=(git conda-zsh-completion)
# 这句放到脚本末
autoload -U compinit && compinit
```

### z

内置插件`z`

提供一个z命令，在常用目录之间跳转。

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

### colored-man

内置插件。给man添加色彩。

### sudo

内置插件。连按两下 Esc 键在命令的开头加上或去掉 sudo 关键字。