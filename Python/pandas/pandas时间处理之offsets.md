利用pandas.tseries.offsets对象可以对时间进行运算


```python
lead_monthly_snapshots_df['snapshot_time'] - pd.tseries.offsets.MonthBegin(1)
```
