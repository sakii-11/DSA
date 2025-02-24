# Stored Procedures, Functions & Event Handling in PostgreSQL

## 1. Stored Procedures
Stored procedures allow executing multiple SQL statements as a single unit.

### 1.1 Creating a Stored Procedure
```sql
CREATE PROCEDURE add_user(IN name TEXT, IN age INT)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO users (name, age) VALUES (name, age);
END;
$$;
```

### 1.2 Calling a Stored Procedure
```sql
CALL add_user('John Doe', 30);
```

### 1.3 Dropping a Stored Procedure
```sql
DROP PROCEDURE add_user;
```

---

## 2. Functions
Functions return a value and can be used within SQL queries.

### 2.1 Creating a Function
```sql
CREATE FUNCTION get_user_age(name TEXT) RETURNS INT
LANGUAGE plpgsql
AS $$
DECLARE
    user_age INT;
BEGIN
    SELECT age INTO user_age FROM users WHERE users.name = name;
    RETURN user_age;
END;
$$;
```

### 2.2 Calling a Function
```sql
SELECT get_user_age('John Doe');
```

### 2.3 Dropping a Function
```sql
DROP FUNCTION get_user_age;
```


