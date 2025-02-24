# PostgreSQL Constraints with Examples

## 1. PRIMARY KEY
Ensures each row has a unique and non-null identifier.
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

## 2. FOREIGN KEY
Ensures referential integrity by linking to another table.
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE
);
```

## 3. UNIQUE
Ensures all values in a column are distinct.
```sql
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE
);
```

## 4. NOT NULL
Ensures a column cannot have NULL values.
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);
```

## 5. CHECK
Enforces a condition on column values.
```sql
CREATE TABLE accounts (
    id SERIAL PRIMARY KEY,
    balance NUMERIC CHECK (balance >= 0)
);
```

## 6. DEFAULT
Provides a default value for a column if no value is specified.
```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    status VARCHAR(20) DEFAULT 'pending'
);
```

## 7. EXCLUSION CONSTRAINT
Ensures that certain rows do not overlap based on a condition.
```sql
CREATE TABLE reservations (
    id SERIAL PRIMARY KEY,
    room INT,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    EXCLUDE USING GIST (room WITH =, tstzrange(start_time, end_time) WITH &&)
);
```

These constraints help maintain data integrity and consistency in PostgreSQL.