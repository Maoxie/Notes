利用`pandas.tseries.offsets`中的对象可以对时间进行运算，例如求某个时间的上一天，可以减去`Day(1)`

```python
from pandas.tseries.offsets import Day
df['now'] - Day(1)
```

`MonthBegin`对象可以求出某月月初的日期（时间不变），而`MonthEnd`对象则用来求月末日期。


```python
from pandas.tseries.offsets import MonthBegin, MonthEnd
MonthBegin(0) # 表示 月初到

# 求下个月1日的相同时刻
df['now'] + MonthBegin(1)
# # 求从该日期及之后日期的第一个月初（如果该日期就是1日，则得到的就是该日期）
df['now'] + MonthBegin(0)
# # 求从该日期之前日期的第一个月初
df['now'] - MonthBegin(1)
# 求上月1日的相同时刻
df['now'] - MonthBegin(2)
```
