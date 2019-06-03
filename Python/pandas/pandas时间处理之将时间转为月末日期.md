> 参考了stackoverflow的如下问题：
>
> [pandas: convert datetime to end-of-month](https://stackoverflow.com/questions/18233107/pandas-convert-datetime-to-end-of-month)

方法一（较快）：

转换为period再转换成timestamp

```python
df.index = df.index.to_period('M').to_timestamp('M')
```

方法二：

利用`pd.tseries.offsets`中的`MonthEnd`对象

```python
df.index = df.index + pd.offsets.MonthEnd(0) 
```

如果需要转为月初时间，可以再用`MonthBegin`对象

```python
df.index = df.index - pd.offsets.MonthBegin(1)
```

