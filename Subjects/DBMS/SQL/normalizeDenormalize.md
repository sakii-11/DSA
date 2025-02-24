# Normalization & Denormalization in PostgreSQL

## 1. Normalization
Normalization is the process of organizing a database to reduce redundancy and improve data integrity by dividing larger tables into smaller ones and defining relationships.

### **Normalization Forms (Examples in PostgreSQL)**

### **1st Normal Form (1NF) - Eliminate Repeating Groups**
**Rule:** Each column must contain atomic (indivisible) values.

**Before 1NF:**
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    subjects TEXT -- 'Math, Science, History'
);
```
**After 1NF (Separate Table for Subjects):**
```sql
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE student_subjects (
    student_id INT REFERENCES students(id),
    subject VARCHAR(50),
    PRIMARY KEY (student_id, subject)
);
```

### **2nd Normal Form (2NF) - Remove Partial Dependencies**
**Rule:** The table must be in 1NF, and all non-key attributes should be fully dependent on the primary key.

**Before 2NF:**
```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    product_id INT,
    product_name VARCHAR(100)
);
```
**Issue:** `product_name` depends only on `product_id`, not `order_id`.

**After 2NF (Separate Products Table):**
```sql
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    product_id INT REFERENCES products(product_id)
);
```

### **3rd Normal Form (3NF) - Remove Transitive Dependencies**
**Rule:** The table must be in 2NF, and all non-key attributes must depend only on the primary key.

**Before 3NF:**
```sql
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT,
    dept_name VARCHAR(100)
);
```
**Issue:** `dept_name` depends on `dept_id`, not directly on `emp_id`.

**After 3NF (Separate Departments Table):**
```sql
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(100)
);

CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(100),
    dept_id INT REFERENCES departments(dept_id)
);
```

### **Boyce-Codd Normal Form (BCNF) - Stronger 3NF**
**Rule:** The table must be in 3NF, and every determinant must be a candidate key.

**Before BCNF:**
```sql
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    instructor VARCHAR(100),
    department VARCHAR(100),
    PRIMARY KEY (course_id, instructor)
);
```
**Issue:** `department` depends on `instructor`, but `instructor` is not a candidate key.

**After BCNF (Separate Instructors Table):**
```sql
CREATE TABLE instructors (
    instructor VARCHAR(100) PRIMARY KEY,
    department VARCHAR(100)
);

CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    instructor VARCHAR(100) REFERENCES instructors(instructor)
);
```

## 2. Denormalization
Denormalization is the process of combining tables to improve read performance at the cost of some redundancy.

### **Example: Join Tables for Faster Queries**
Instead of separate `orders` and `products` tables (from 2NF example), store product details directly in `orders`.

```sql
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100),
    product_id INT,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);
```
**Advantage:** Faster queries, as no `JOIN` is needed.

**Disadvantage:** If product details change, updating all rows can be inefficient.

## **When to Normalize vs. Denormalize?**
| Situation | Normalization | Denormalization |
|-----------|--------------|----------------|
| Data integrity is crucial | ✅ | ❌ |
| Minimize redundancy | ✅ | ❌ |
| Improve read performance | ❌ | ✅ |
| Optimize write-heavy applications | ✅ | ❌ |
| Reduce complex joins | ❌ | ✅ |

**Conclusion:**
- Use **normalization** for better data consistency and integrity.
- Use **denormalization** when optimizing for read-heavy applications where performance matters more than redundancy.


