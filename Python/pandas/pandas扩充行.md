## 简单Index

对于简单的时间序列索引，用reindex可以实现行的扩充。

## MultiIndex

对于MultiIndex，只在某个level上应用reindex不会使行扩充，只会对存在的行进行排序。因此需要生成完整的MultiIndex索引。

为此，可以使用pd.MultiIndex.