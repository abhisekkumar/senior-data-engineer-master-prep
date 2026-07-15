-- Ranking functions on synthetic employee data.
-- ROW_NUMBER chooses exactly one row; RANK leaves gaps after ties;
-- DENSE_RANK does not leave gaps.
SELECT
    employee_id,
    department,
    salary,
    ROW_NUMBER() OVER (PARTITION BY department ORDER BY salary DESC) AS row_number_rank,
    RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS standard_rank,
    DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS dense_rank
FROM employee_salary;

-- Highest-paid employee(s) per department, including ties.
WITH ranked AS (
    SELECT
        employee_id,
        department,
        salary,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
    FROM employee_salary
)
SELECT employee_id, department, salary
FROM ranked
WHERE salary_rank = 1;

-- Second-highest distinct salary per department.
WITH ranked AS (
    SELECT
        employee_id,
        department,
        salary,
        DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS salary_rank
    FROM employee_salary
)
SELECT employee_id, department, salary
FROM ranked
WHERE salary_rank = 2;
