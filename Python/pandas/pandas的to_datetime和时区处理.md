# pandas库时间和时区处理

`pandas.to_datetime`用来将时间数据转为pandas的datetime类型

```python
# 转换的为时间戳数据时，提供时间戳的精度
datetime_df = pd.to_datetime(df['timestamp_column'], unit='ms')
```

`tz_localize`用于设定时区，`tz_convert`用于转换时区

`DataFrame.tz_localize`和`DataFrame.tz_convert`用于转换时间类型的index的时区，如果需要转换数据列的时区，用`DataFrame.dt.tz_localize`和`DataFrame.dt.tz_convert`

```python
datetime_df.dt.tz_localize('UTC')\
    .dt.tz_convert('Asia/Shanghai')\
    .dt.tz_localize(None)
```

时区设为`None`表示取消时区