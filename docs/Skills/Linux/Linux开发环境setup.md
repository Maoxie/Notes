# Linux 开发环境 setup

## (1) Recommend
> [配置apt镜像](https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/)

- Dependencies
```bash
# Ubuntu
sudo apt-get update
sudo apt-get install autoconf automake build-essential cmake git libass-dev libbz2-dev libfontconfig1-dev libfreetype6-dev libfribidi-dev libharfbuzz-dev libjansson-dev liblzma-dev libmp3lame-dev libogg-dev libopus-dev libsamplerate-dev libspeex-dev libtheora-dev libtool libtool-bin libvorbis-dev libx264-dev libxml2-dev m4 make nasm patch pkg-config tar yasm zlib1g-dev python python3 python3-pip python3-dev python3-setuptools
```
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- git: 最新版本
    - [install](https://git-scm.com/download/linux)
    - [build from source](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [zsh](https://www.zsh.org/)
    - [oh-my-zsh](https://github.com/Maoxie/Notes/blob/master/docs/Skills/Linux/zsh%E5%B8%B8%E7%94%A8%E6%8F%92%E4%BB%B6.md)
- [Node.js](https://nodejs.org/en/download/)
- Mackup: 配置备份/同步
    - [Instruction](https://github.com/Maoxie/Notes/blob/master/docs/Skills/Linux/Mackup%20%E5%90%8C%E6%AD%A5linux%E9%85%8D%E7%BD%AE.md)
- neovim
    - [Instruction](https://github.com/Maoxie/Notes/blob/master/docs/Skills/Software-Specific/Neovim/%E5%AE%89%E8%A3%85Neovim.md)
- [global gitignore](https://github.com/Maoxie/Notes/blob/master/docs/Skills/Git/global%20gitignore.md)

## (2) CLI tools
[neofetch](https://github.com/dylanaraps/neofetch): 获取并打印系统信息

[thefuck](https://github.com/nvbn/thefuck#installation): 纠正输错的命令

[tldr](https://github.com/tldr-pages/tldr#how-do-i-use-it):

```bash
pip3 install tldr
```