利用pandas.tseries.offsets


```python
lead_monthly_snapshots_df['snapshot_time'] - pd.tseries.offsets.MonthBegin(1)
```
