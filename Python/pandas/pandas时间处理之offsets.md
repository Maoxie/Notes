利用`pandas.tseries.offsets`中的对象可以对时间进行运算，例如求某个时间的上一天，可以减去`Day(1)`

```python

```




```python
lead_monthly_snapshots_df['snapshot_time'] - pd.tseries.offsets.MonthBegin(1)
```
