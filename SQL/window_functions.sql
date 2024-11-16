-- Syntax
function_name (expression) OVER (PARTITION BY column ORDER BY column)

-- Window functions performs calculations across rows without aggregating them into single row
-- Analyze and rank data, such as cumulative sum, calculating running average, and ranks

-- 1. ROW_NUMBER()
-- ASSIGN a unique sequential number to each row within partition

-- This will assign a row number to each employee in same dept based on their salary
SELECT 
    name, 
    department, 
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS ROW_NUMBER
FROM EMPLOYEE

-- 2. RANK()
-- Ranks rows within a partition, with gaps in the ranking for ties. 
-- If two values are same, they will receive same rank, and the next rank will skip a number

SELECT 
    name,
    department,
    salary,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) as rank
FROM EMPLOYEE

-- 3. DENSE_RANK()
-- Similar to RANK(), but without gaps in the ranking. 
-- Tied values will share the same rank, and the next rank will continue sequentially

-- 4. LAG()
-- Provides access to a row at a specified physical offset before the current row in the s=result set

SELECT
    name, 
    salary,
    dapartment,
    LAG(salary, 1) OVER (PARTITION BY department ORDER BY salary) AS previous_salary
FROM EMPLOYEE


-- 5. LEAD()
-- Similar to LAG(), but it accesses the next row data

SELECT
    name,
    salary,
    department,
    LEAD(salary, 1) OVER (PARTITION BY department ORDER BY salary) AS next_salary
FROM EMPLOYEE


-- Aggregate Functions with Window Functions
-- SUM(), MIN(), MAX(), AVG()

-- calculate the average of set of values

SELECT
    name,
    department,
    salary,
    AVG(salary) OVER (PARTITION BY department) AS average_salary,
    MIN(salary) OVER (PARTITION BY department) AS min_salary,
    MAX(salary) OVER (PARTITION BY department) AS max_salary
FROM employee


-- Note - Window functions can be computationally expensive, especially when combined with large 
-- datasets or comple partitions, use them wisely
