# alembic 基本命令

```bash
# 自动生成迁移脚本
 alembic revision --autogenerate -m 'create_user_table'
```



```bash
# 更新
alembic upgrade head    # 到最新版
alembic upgrade <版本号>

# 降级
alembic downgrade head  # 到最初版
alembic downgrade <版本号>

# 离线更新（生成sql）
alembic upgrade <版本号> --sql > migration.sql
# 从特定起始版本生成sql
alembic upgrade <版本一>:<版本二> --sql > migration.sql

# 查看版本历史
alembic history
```
