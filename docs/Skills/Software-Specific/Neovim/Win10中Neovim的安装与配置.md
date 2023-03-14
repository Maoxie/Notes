# Win10 中 Neovim的安装与配置

> [Windows 10 系统下 Neovim 安装与配置 - jdhao's digital space](https://jdhao.github.io/2018/11/16/neovim_configuration_windows-zh/#fn:1)

## 1. 安装

下载编译好的安装包，直接解压安装包即可完成安装：

[equalsraf/neovim-qt: Neovim client library and GUI, in Qt5. (github.com)](https://github.com/equalsraf/neovim-qt)

为了确保在命令行可以使用 `nvim` 这个命令打开 Neovim，将安装路径添加到`PATH`中。

## 2. 配置

### 2.1 配置文件在哪里

Neovim 使用了和 Vim 不同的配置文件名称以及配置文件存放位置，根据 Neovim [官方文档](https://neovim.io/doc/user/starting.html#base-directories)，Neovim 的配置文件应该命名为 `init.vim`，并且应该放在 `~/AppData/Local/nvim` 目录下。（打开 Neovim，使用 `:echo stdpath('config')` 可以查看该目录的具体位置）
