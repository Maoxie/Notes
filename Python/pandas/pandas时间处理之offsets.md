利用`pandas.tseries.offsets`中的对象可以对时间进行运算，例如求某个日期上一天，可以用Day


```python
lead_monthly_snapshots_df['snapshot_time'] - pd.tseries.offsets.MonthBegin(1)
```
