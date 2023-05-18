# Linux 开发环境 setup

## (1) Recommend

> [配置apt镜像](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

### Dependencies

```bash
# Ubuntu
sudo apt-get update
sudo apt-get install autoconf automake build-essential cmake git libass-dev libbz2-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev libharfbuzz-dev libjansson-dev liblzma-dev libmp3lame-dev libogg-dev libopus-dev libsamplerate-dev libspeex-dev libtheora-dev libtool libtool-bin libvorbis-dev libx264-dev libxml2-dev m4 make nasm patch pkg-config tar yasm zlib1g-dev python python3 python3-pip python3-dev python3-setuptools zip
```

### Miniconda

- [Linux Installers](https://docs.conda.io/en/latest/miniconda.html#linux-installers)

### git 升级版本

- [install](https://git-scm.com/download/linux)
- [build from source](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### zsh

- 安装 [zsh](https://www.zsh.org/)
- [oh-my-zsh](https://github.com/Maoxie/Notes/blob/master/docs/Skills/Linux/zsh%E5%B8%B8%E7%94%A8%E6%8F%92%E4%BB%B6.md)

### Node.js

- 利用[NVM](https://github.com/nvm-sh/nvm#installing-and-updating)安装
- 直接安装[Download | node.js](https://nodejs.org/en/download/)

### Mackup: 配置备份/同步

- [Instruction](https://github.com/Maoxie/Notes/blob/master/docs/Skills/Linux/Mackup%20%E5%90%8C%E6%AD%A5linux%E9%85%8D%E7%BD%AE.md)

### neovim

- [Installing-Neovim](https://github.com/neovim/neovim/wiki/Installing-Neovim#ubuntu)

### 配置全局 gitignore

- 配置方法: [global gitignore](https://github.com/Maoxie/Notes/blob/master/docs/Skills/Git/global%20gitignore.md)

## (2) CLI tools

[neofetch](https://github.com/dylanaraps/neofetch): 获取并打印系统信息

[thefuck](https://github.com/nvbn/thefuck#installation): 纠正输错的命令

[tldr](https://github.com/tldr-pages/tldr#how-do-i-use-it):

```bash
pip3 install tldr
```

[exa](https://the.exa.website/install/linux): a modern replacement for `ls`

```bash
wget https://github.com/ogham/exa/releases/download/v0.10.0/exa-linux-x86_64-v0.10.0.zip
unzip exa-linux-x86_64-v0.10.0.zip -d exa
sudo install -o root -g root -m 0755 exa/bin/exa /usr/local/bin/exa
```

[bottom](https://github.com/ClementTsang/bottom?ref=itsfoss.com#debianubuntu): 图形化进程、系统monitor
