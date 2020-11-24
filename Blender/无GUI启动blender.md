## headless方式启动 blender

```bash
blender -b
```

 ## 启动blender的同时执行 python 脚本

```bash
blender -b -P my_script.py
```

### 给脚本传参

blender会把第一个`--`之后的参数传给脚本，但在脚本内部会获取到全部的参数而非只有`--`之后的参数，需要自己过滤掉它们。

```bash
blender -b -P my_script.py -- --number 5 --save '/Users/Jenny/Desktop/cube.obj'
```

## 打开python shell

```bash
blender -b --python-console
```

