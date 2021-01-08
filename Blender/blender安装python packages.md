```python
import subprocess
import sys
from pathlib import Path
 
python_exe = Path(sys.prefix) / 'bin' / 'python3.7m'	# 具体路径
 
# 'C:\\Program Files\\blender283\\2.83\\python\\bin\\python.exe'
assert python_exe.exists()

# upgrade pip
subprocess.call([python_exe, "-m", "ensurepip"])
subprocess.call([python_exe, "-m", "pip", "install", "--upgrade", "pip"])
 
# install required packages
subprocess.call([python_exe, "-m", "pip", "install", "package_name"])
```

## 通过 get-pip.py 安装 pip

如果blender是通过snap安装的，可能会有Read Only的问题，可以用以下方式安装pip

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# 确定具体路径
/snap/blender/58/2.83/python/bin/python3.7m get-pip.py
```

