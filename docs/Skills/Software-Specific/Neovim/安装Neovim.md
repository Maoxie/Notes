# 安装Neovim

> [install-from-package](https://github.com/neovim/neovim/wiki/Installing-Neovim#install-from-package)

安装 python2-provider & python3-provider

```bash
pip2 install --user --upgrade pynvim
pip3 install --user --upgrade pynvim
```

安装 vim-plug 

> [junegunn/vim-plug](https://github.com/junegunn/vim-plug#neovim)

```bash
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

安装后自检，执行:

```
:health
```
