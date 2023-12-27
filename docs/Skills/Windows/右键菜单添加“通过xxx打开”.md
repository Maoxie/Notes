# 右键菜单添加“通过 xxx 打开”

以添加“通过 Neovim 打开”为例。

## 1. 打开注册表编辑器

win +R，输入 `regedit`。

定位到 `HKEY_CLASSES_ROOT\*\shell`

## 2. 新建菜单项

在shell下新建`项`，命名为 `Open with neovim`

可在右侧窗口中修改 `(默认)` 的值为菜单显示名称，例如：

```powershell
通过 Neovim 打开
```

## 3. 设置命令

在 `Open with neovim` 下新建`项`，命名为`command`。

在右侧窗口中修改 `(默认)` 的值为启动命令，例如：

```powershell
C:\Program Files\Neovim\bin\nvim-qt.exe %1
```

## 4. 设置图标

在 `Open with neovim` 下新建`可扩充字符串值`项，命名为 `Icon`。

在右侧窗口中修改 `(默认)` 的值为图标或可执行文件的路径，例如：

```powershell
C:\Program Files\Neovim\bin\nvim-qt.exe
```
