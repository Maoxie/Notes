用`pandas.DataFrame.sort_index`方法可以先对DataFrame进行排序。

当需要对某一级索引进行自定义顺序的排序时，可以用`pandas.DataFrame.reindex`方法

例如：

```python
					month	2018-12-31	2019-01-31	2019-02-28	...	2019-04-30	2019-05-31	2019-06-30
category	商机状态	线索状态	商机状态	差旅	总费用	招待	拜访次数	线索状态	项目拜访总次数	商机状态	...	线索状态	项目拜访总次数	商机状态	差旅	总费用	拜访次数	线索状态	项目拜访总次数	商机状态	线索状态
employee_id	chinese_name	lead_code	lead_name	province	city																					
132	梅琪		NaN	NaN	NaN	NaN	NaN	NaN	2191.00	2191.00	0.0	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	0.00	0.00	NaN	NaN	NaN	NaN	NaN
PL20170210	莉莉一期	上海市	上海市	NaN	NaN	NaN	754.00	754.00	NaN	1.0	NaN	1.0	NaN	...	NaN	NaN	NaN	NaN	0.00	NaN	NaN	NaN	激发需求	线索(待分配)
PL20170241	海家一期	江苏省	无锡市	NaN	NaN	NaN	NaN	0.00	NaN	NaN	NaN	NaN	NaN	...	NaN	NaN	NaN	NaN	0.00	NaN	NaN	NaN	立项	商机
```



