## 问题来源

项目根目录为project，其中的scripts目录内存放有一系列脚本`a.py`,`b.py`,`c.py`等，其中脚本的运行需要import 项目中的某些模块。

```
project
 ├─scripts
 │  ├─a.py
 │  ├─b.py
 │  └─c.py
 ├─apps
 │  ├─module_1
 │  │  ├─...
 │  │  └─...
 │  ├─module_2
 ...
```

为此，在import之前，需要把项目的根目录加入到脚本运行时的path中（`sys.path.append`），需要确定脚本所在目录，由此推出上一级目录的路径。

## 一开始的写法

```python
project_base = Path(__file__).parents[1]
sys.path.append(str(project_base))
```

问题：`__file__`得到的是相对于当前工作路径的脚本文件的相对路径。

通过`python scripts/a.py`运行脚本时，`__file__ == "scripts/a.py"`。

通过`python a.py`运行脚本时，`__file__ == "a.py"`。

当`__file__ == "a.py"`时，`Path(__file__).parents[0]`命令因无法获取到父级目录而报错。

## 第二版的写法

```python
project_base = Path(os.getcwd()).parents[0]
sys.path.append(str(project_base))
```

现在在scripts下面运行脚本没有问题了，但是通过Pycharm调试时，Pycharm会在项目根目录下启动脚本，因此`os.getcwd()`得到的是项目根目录的路径，此时获取的`project_base`就不对了。

## 正确写法

```python
project_base = Path(__file__).resolve().parents[1]
sys.path.append(str(project_base))

# python早期版本没有pathlib库，利用os库的等价写法如下：
project_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_base)
```

利用Path().resovle()或os.path.abspath获取绝对路径，然后再获取父级目录。



