## 简单Index

对于简单的时间序列索引，用reindex可以实现行的扩充。

## MultiIndex

对于MultiIndex，只在某个level上应用reindex不会使行扩充，只会对存在的行进行排序。因此需要生成完整的MultiIndex索引。

为此，可以结合`pandas.pivot_table`将需要扩充列索引变为某个轴上的简单索引，再用`reindex`方法扩充，最后用`stack`方法恢复原先的结构。

这种做法会丢失一些列，因此最后还需要用`merge`方法将丢失的列信息补充回来

例如:

```python
# 扩充 monthly_data_df 的 start_time 列
# 用于扩充的新索引数据为 month_end_date_index
# 扩充后的结果为 time_expanded_df
time_expanded_df = pd.pivot_table(monthly_data_df, index=['start_time'],
                                  columns=['employee_id', 'lead_code'],
                                  values=['visit_times']
                                  ).reindex(month_end_date_index)
time_expanded_df = time_expanded_df.stack(['employee_id', 'lead_code'], dropna=False
                                          ).reset_index().rename({'level_0': 'start_time'}, axis=1)
time_expanded_df['visit_times'] = time_expanded_df['visit_times'].fillna(0)
time_expanded_df = time_expanded_df.merge(leads_info, on=['employee_id', 'lead_code'])

```



