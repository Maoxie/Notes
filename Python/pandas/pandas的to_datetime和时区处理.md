# pandas库时间和时区处理

`pandas.to_datetime`用来将时间数据转为pandas的datetime类型

```python
df['timestamp_column'] = \
pd.to_datetime(df['timestamp_column'], unit='ms')	# 指定时间戳的精度为ms
```

