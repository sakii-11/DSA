# Joins in PostgreSQL

## 1. INNER JOIN
Returns only matching rows from both tables.

```sql
SELECT users.id, users.name, orders.order_id
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

## 2. LEFT JOIN (or LEFT OUTER JOIN)
Returns all rows from the left table and matching rows from the right table. If no match is found, NULL is returned.

```sql
SELECT users.id, users.name, orders.order_id
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

## 3. RIGHT JOIN (or RIGHT OUTER JOIN)
Returns all rows from the right table and matching rows from the left table. If no match is found, NULL is returned.

```sql
SELECT users.id, users.name, orders.order_id
FROM users
RIGHT JOIN orders ON users.id = orders.user_id;
```

## 4. FULL JOIN (or FULL OUTER JOIN)
Returns all rows when there is a match in either table. If no match, NULL is returned for missing values.

```sql
SELECT users.id, users.name, orders.order_id
FROM users
FULL JOIN orders ON users.id = orders.user_id;
```

## 5. CROSS JOIN
Returns the Cartesian product of both tables (each row from the first table is combined with every row from the second table).

```sql
SELECT users.id, users.name, orders.order_id
FROM users
CROSS JOIN orders;
```

## 6. SELF JOIN
A table is joined with itself. Useful for hierarchical data (e.g., employees and managers).

```sql
SELECT e1.id AS employee_id, e1.name AS employee_name, e2.name AS manager_name
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```