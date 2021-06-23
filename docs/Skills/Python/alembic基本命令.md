# alembic 基本命令

```bash
 alembic revision --autogenerate -m 'init'
```



```bash
# 更新到最新版
alembic upgrade head
# 降级到最初版
alembic downgrade head
# 离线更新（生成sql）
alembic upgrade 版本号 --sql > migration.sql
# 从特定起始版本生成sql
alembic upgrade 版本一:版本二 --sql > migration.sql
```
