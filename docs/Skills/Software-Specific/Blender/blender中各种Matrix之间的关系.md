# Blender中各种Matrix之间的关系

## 0. bpy_types

- `bpy_types.Object`

```python
>>> type(bpy.data.objects['Armature'])
<class 'bpy_types.Object'>
```

- `bpy.types.Armature`

```python
>>> type(bpy.data.armatures['Armature'])
<class 'bpy.types.Armature'>
>>> type(bpy.data.objects['Armature'].data)
<class 'bpy.types.Armature'>
```

- `bpy.types.Pose` <- `bpy.types.Object`.pose

```python
>>> type(bpy.data.objects['Armature'].pose)
<class 'bpy.types.Pose'>
```

- `bpy_types.PoseBone` <- `bpy.types.Pose`.bones[0]

```python
>>> type(bpy.data.objects['Armature'].pose.bones[0])
<class 'bpy_types.PoseBone'>
```

- `bpy_types.Bone` <- `bpy.types.Armature`.bones[0]
- `bpy_types.Bone` <- `bpy.types.PoseBone`.bone

```python
>>> type(bpy.data.armatures['Armature'].bones[0])
<class 'bpy_types.Bone'>
>>> type(bpy.data.objects['Armature'].data.bones[0])
<class 'bpy_types.Bone'>
>>> type(bpy.data.objects['Armature'].pose.bones[0].bone)
<class 'bpy_types.Bone'>
```


## 1. matrix

> [How can I manually calculate bpy.types.PoseBone.matrix using Blender's Python API? - Blender Stack Exchange](https://blender.stackexchange.com/questions/44637/how-can-i-manually-calculate-bpy-types-posebone-matrix-using-blenders-python-ap)

> [Blender Manual - Space types](https://docs.blender.org/manual/en/latest/animation/constraints/interface/common.html#space-types)

均为4×4矩阵。

- `Bone.matrix_local`：bone在**ARMATURE SPACE**中的无pose矩阵；等价于**在Rest Position状态下**的 `PoseBone.matrix`。

```python
>>> bpy.data.objects['Armature'].data.bones["Bone"].matrix_local \
... == bpy.data.objects['Armature'].pose.bones["Bone"].matrix
True
```

- `PoseBone.matrix_basis`：bone在**BONE SPACE**中的局部变换矩阵，不受父骨骼影响。

```python
>>> bpy.data.objects['Armature'].pose.bones["Bone"].matrix_basis.translation \
... == bpy.data.objects['Armature'].pose.bones["Bone"].matrix_basis.to_translation() \
... == bpy.data.objects['Armature'].pose.bones["Bone"].location
True

>>> bpy.data.objects['Armature'].pose.bones["Bone"].matrix_basis.to_quaternion() \
... == bpy.data.objects['Armature'].pose.bones["Bone"].rotation_quaternion
True

>>> bpy.data.objects['Armature'].pose.bones["Bone"].matrix_basis.to_scale() \
... == bpy.data.objects['Armature'].pose.bones["Bone"].scale
True
```

- `PoseBone.matrix`：bone在**ARMATURE SPACE**中的pose矩阵。
- `Object.matrix_world`：object在**WORLD SPACE**中的变换矩阵。

### 矩阵间的变换关系

从 `Bone.matrix_local` 和 `PoseBone.matrix_basis` 出发计算 `PoseBone.matrix`：

```python
def matrix_world(armature_ob, bone_name):
    local = armature_ob.data.bones[bone_name].matrix_local
    basis = armature_ob.pose.bones[bone_name].matrix_basis

    parent = armature_ob.pose.bones[bone_name].parent
    if parent is None:
        return local * basis
    else:
        parent_local = armature_ob.data.bones[parent.name].matrix_local
        return matrix_world(armature_ob, parent.name) * (parent_local.inverted() * local) * basis
```

思路：从 BONE SPACE 逐级变换到父骨骼的 BONE SPACE，最终到达根骨骼的 BONE SPACE 即为 ARMATURE SPACE。

- basis：当前骨骼在自己的bone space中的变换矩阵。
- local * basis：当所有祖先骨骼都在rest position状态下时，当前骨骼在armature space中的变换矩阵。
- (parent_local.inverted() * local) * basis：父骨骼在rest position状态下时，当前骨骼在父骨骼的bone space中的变换矩阵。
- parent_basis * (parent_local.inverted() * local) * basis：当前骨骼在父骨骼的bone space中的变换矩阵。

