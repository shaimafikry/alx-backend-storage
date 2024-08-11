### 1. Creating Tables with Constraints in MySQL

When creating tables in MySQL, you can add various constraints to ensure the integrity and validity of the data. Here are some common constraints:

- **PRIMARY KEY**: Ensures that each value in a column (or set of columns) is unique and not NULL.
- **FOREIGN KEY**: Ensures that the value in a column matches a value in another table's column.
- **UNIQUE**: Ensures all values in a column (or a combination of columns) are unique.
- **NOT NULL**: Ensures a column cannot have NULL values.
- **CHECK**: Ensures that values in a column meet a specific condition.

**Example:**
```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
```

### 2. Optimizing Queries by Adding Indexes

Indexes are used to speed up the retrieval of rows by using a pointer. An index can be created on one or more columns of a table.

Selecting what to index is probably the most challenging part to indexing your databases. Determining what is important enough to index and what is benign enough to not index. Generally speaking, indexing works best on those columns that are the subject of the WHERE clauses in your commonly executed queries. 

- **CREATE INDEX**: Creates a new index.
- **UNIQUE INDEX**: Ensures that all values in the indexed column(s) are unique.

**Example:**
```sql
CREATE INDEX idx_employee_lastname ON employees(last_name);
```

**Considerations:**
- Indexes improve read performance but can slow down write operations (INSERT, UPDATE, DELETE).
- Use indexes on columns that are frequently used in `WHERE`, `JOIN`, and `ORDER BY` clauses.

<h3><a href = 'https://www.youtube.com/watch?v=BIlFTFrEFOI'>Visualization about indexing </a></h3>

### 3. Stored Procedures and Functions in MySQL

- **Stored Procedures**: A stored procedure is a prepared SQL code that you can save and reuse. You can pass parameters to it, and it can contain complex logic.

**Example of a Stored Procedure:**
```sql
DELIMITER //
CREATE PROCEDURE GetEmployeeSalary(IN emp_id INT)
BEGIN
    SELECT salary FROM employees WHERE employee_id = emp_id;
END //
DELIMITER ;
```

- **Functions**: Similar to stored procedures but returns a single value and can be used in SQL statements.

**Example of a Function:**
```sql
DELIMITER //
CREATE FUNCTION GetFullName(emp_id INT) RETURNS VARCHAR(100)
BEGIN
    DECLARE full_name VARCHAR(100);
    SELECT CONCAT(first_name, ' ', last_name) INTO full_name 
    FROM employees WHERE employee_id = emp_id;
    RETURN full_name;
END //
DELIMITER ;
```

### 4. Views in MySQL

A view is a virtual table based on the result of a SQL query. It can simplify complex queries, encapsulate logic, and provide security by restricting access to specific data.

**Creating a View:**
```sql
CREATE VIEW employee_view AS
SELECT employee_id, first_name, last_name, department_id, salary
FROM employees
WHERE salary > 50000;
```

**Using a View:**
```sql
SELECT * FROM employee_view;
```

### 5. Triggers in MySQL

Triggers are special types of stored procedures that automatically execute in response to certain events on a table (INSERT, UPDATE, DELETE).

**Creating a Trigger:**
```sql
CREATE TRIGGER before_employee_insert
BEFORE INSERT ON employees
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Salary cannot be negative';
    END IF;
END;
```

**Types of Triggers:**
- **BEFORE Trigger**: Executes before the triggering event.
- **AFTER Trigger**: Executes after the triggering event.

Triggers can help maintain data integrity and enforce business rules automatically.
Sure! Let’s break down the SQL query:

```sql
SELECT band_name, COALESCE(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
```

### Explanation

1. **`SELECT band_name, COALESCE(split, 2020) - formed AS lifespan`**:
   - **`band_name`**: This selects the `band_name` column from the `metal_bands` table.
   - **`COALESCE(split, 2020) - formed`**:
     - **`COALESCE(split, 2020)`**: The `COALESCE()` function returns the first non-null value among its arguments. In this case, if `split` is `NULL`, it will use `2020` instead. This handles cases where the `split` year might be missing (i.e., the band hasn’t split or the `split` year is unknown).
     - **`- formed`**: Subtracts the `formed` year from the result of `COALESCE(split, 2020)`. This calculates the lifespan of the band based on the `split` year or `2020` if `split` is `NULL`.
   - **`AS lifespan`**: This aliases the result of the calculation as `lifespan`.

2. **`FROM metal_bands`**:
   - Specifies that the data is coming from the `metal_bands` table.

3. **`WHERE style LIKE '%Glam rock%'`**:
   - **`LIKE '%Glam rock%'`**: The `LIKE` operator is used for pattern matching. The `%` symbols are wildcards that match any sequence of characters. This condition filters the rows to include only those where the `style` column contains the substring `'Glam rock'` anywhere within it. It allows for variations like `'Glam rock'`, `'Heavy Glam rock'`, or `'Glam rock and Metal'`.

### Summary

This query calculates the `lifespan` of bands where the `style` contains `'Glam rock'`. If a band has a `NULL` value for the `split` year, it uses `2020` as a default value to compute the lifespan. The result is a list of band names and their calculated lifespan.
