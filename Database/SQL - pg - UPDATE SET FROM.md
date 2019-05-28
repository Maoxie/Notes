写法1（b是单表）

```sql
update a set a.a1=b.b1,a.a2=b.b2 from b 
where b1=1 and a1=1
```

写法2（b是子查询）

```sql
update a set a.a1=b.b1,a.a2=b.b2 from (
	select * from t
    where t.id = 1
) b
where b1=1 and a1=1
```

