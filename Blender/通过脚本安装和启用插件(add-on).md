### 2.8版本

```python
import bpy

bpy.ops.preferences.addon_install(filepath='path/to/add-on.zip')
bpy.ops.preferences.addon_enable(module='name-of-add-on')
bpy.ops.wm.save_userpref()
```

### 2.7 版本

```python
import bpy

bpy.ops.wm.addon_install(filepath='path/to/add-on.zip')
bpy.ops.wm.addon_enable(module='name-of-add-on')
bpy.ops.wm.save_userpref()
```

