## 1. Maya
### (1) 世界坐标系
$$
\begin{aligned}
	&y \\
	&\uparrow \\
	&\odot \longrightarrow x \\
z \swarrow\ & \\
\end{aligned}
$$

### (2) 旋转
外旋XYZ：
$$
R = R_z \cdot R_y \cdot R_x
$$

|       |     |
| ----- | --- |
| Yaw   | Y   |
| Pitch | X   |
| Roll  | Z   |

## 2. Blender
### (1) 世界坐标系
$$
\begin{aligned}
	&z \\
	&\uparrow \\
	&\odot \longrightarrow y \\
x \swarrow\ & \\
\end{aligned}
$$

### (2) 旋转
默认为外旋XYZ
$$
R = R_z \cdot R_y \cdot R_x
$$
动画pose中的旋转默认为四元数

## 3. UE
### (1) 世界坐标系
**左手系**

$$
\begin{aligned}
&z \\
&\uparrow \nearrow\ x\\
&\otimes \longrightarrow y \\
\end{aligned}
$$

### (2) 旋转
用左手定则确定旋转角方向（**与右手系的方向相反**）

外旋XYZ:
$$
R = R_z \cdot R_y \cdot R_x
$$

|       |     |
| ----- | --- |
| Yaw   | Z   |
| Pitch | Y   |
| Roll  | X   |

## 4. MeshLab
### (1) 世界坐标系
$$
\begin{aligned}
	&y \\
	&\uparrow \\
	&\odot \longrightarrow x \\
z \swarrow\ & \\
\end{aligned}
$$
同Maya

## 5. SMPL(X)
### (1) 世界坐标系
坐标系原点在胸腔内部，使得模型各顶点 `(x-mean, y-mean, z-mean) = (0,0,0)`
$$
\begin{aligned}
	&y \\
	&\uparrow \\
	&\odot \longrightarrow x \\
z \swarrow\ & \\
\end{aligned}
$$
同Maya

### (2) 旋转
同Maya

## 6. Pytorch3D
### (1) 世界坐标系
$$
\begin{aligned}
&y \\
&\uparrow \nearrow\ z\\
x \longleftarrow &\otimes \\
\end{aligned}
$$

### (2) 旋转
矩阵或四元数表示

## 7. OpenCV (pyrenderer)
### (1) 相机坐标系
以相机位置为原点，+z为远离相机方向

$$
\begin{aligned}
	&\ \ \nearrow z \\
	&\otimes \longrightarrow x \\
	&\downarrow \\
	&y
\end{aligned}
$$
### (2) 旋转
矩阵形式

## 8. OpenGL
### (1) 世界坐标系
$$
\begin{aligned}
	&y \\
	&\uparrow \\
	&\odot \longrightarrow x \\
z \swarrow\ & \\
\end{aligned}
$$
同Maya

### (2) 旋转
内旋YZX：
$$
R = R_y \cdot R_z \cdot R_x
$$

|       |     |
| ----- | --- |
| Yaw   | Y   |
| Pitch | X   |
| Roll  | Z   |
