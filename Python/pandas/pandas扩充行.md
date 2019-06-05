## 简单Index

对于简单的时间序列索引，用reindex可以实现行的扩充。

## MultiIndex

对于MultiIndex，只在某个level上应用reindex不会使行扩充，只会对存在的行进行排序。因此需要生成完整的MultiIndex索引。

为此，可以使用`pd.MultiIndex.from_product`

例如:

```python
# 原有索引列
In [1]: df.index.names
Out[1]:
FrozenList(['employee_id', 'lead_code', 'start_time'])
# 
In [1]: df.index.names.unique()
Out[1]: 
DatetimeIndex(['2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30',
               '2019-05-31'],
              dtype='datetime64[ns]', name='start_time', freq=None)
# 需要扩充start_time这一列的索引，使对于所有的'employee_id'和'lead_code'，都有如下时间的行，如下
time_range = ['2019-01-31', '2019-02-28', '2019-03-31', '2019-04-30',
               '2019-05-31']

```



