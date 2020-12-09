```python
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



