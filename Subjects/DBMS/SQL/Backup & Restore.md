# PostgreSQL Backup & Restore

## 1. Backup a PostgreSQL Database

### 1.1 Backup to a Plain SQL File
```sh
pg_dump -U username -d database_name -f backup.sql
```

### 1.5 Backup Specific Table
```sh
pg_dump -U username -d database_name -t table_name -f table_backup.sql
```

---

## 2. Restore a PostgreSQL Database

### 2.1 Restore from a Plain SQL File
```sh
psql -U username -d database_name -f backup.sql
```

### 2.5 Restore Specific Table
```sh
pg_restore -U username -d database_name --table=table_name backup.tar
```

---

## Conclusion
- Use `pg_dump` for backups.
- Use `pg_restore` or `psql` for restoring.
- Always test backups by restoring to a test environment.
- Use compressed format (`-F c`) for faster backup & restore.

