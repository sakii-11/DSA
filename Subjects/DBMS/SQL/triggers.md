# PostgreSQL Triggers

## 1. What is a Trigger?
A **trigger** in PostgreSQL is a database callback function that automatically executes when a specified event occurs on a table.

---

## 2. Creating a Trigger
### **2.1 Basic Syntax**
```sql
CREATE TRIGGER trigger_name
{ BEFORE | AFTER | INSTEAD OF } { INSERT | UPDATE | DELETE }
ON table_name
FOR EACH { ROW | STATEMENT }
EXECUTE FUNCTION function_name();
```

---

## 3. Example: Creating a Trigger
Use cases for triggers (e.g., logging, data validation)
### **3.1 Step 1: Create a Function**
A trigger needs a function to execute. Below, we create a function that logs changes in an `audit_log` table whenever an `employees` table is updated.

```sql
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    employee_id INT,
    action TEXT,
    modified_at TIMESTAMP DEFAULT NOW()
);
```

```sql
CREATE FUNCTION log_employee_update() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO audit_log (employee_id, action, modified_at)
    VALUES (NEW.id, 'UPDATED', NOW());
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

---

### **3.2 Step 2: Create a Trigger**
Now, we create a trigger that calls the function when an update happens.

```sql
CREATE TRIGGER employee_update_trigger
AFTER UPDATE ON employees
FOR EACH ROW
EXECUTE FUNCTION log_employee_update();
```

---

## 4. Deleting a Trigger
To remove a trigger, use:
```sql
DROP TRIGGER trigger_name ON table_name;
```
**Example:**
```sql
DROP TRIGGER employee_update_trigger ON employees;
```

To remove the trigger function:
```sql
DROP FUNCTION log_employee_update();
```

---

## 5. Viewing Triggers
To list all triggers in the database:
```sql
SELECT * FROM information_schema.triggers WHERE trigger_schema = 'public';
```

---

## 6. Conclusion
- Triggers **automate actions** on database changes.
- Use `BEFORE`, `AFTER`, or `INSTEAD OF` depending on the requirement.
- Always ensure triggers do not cause **recursive calls** or **performance issues**.

