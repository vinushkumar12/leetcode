# Write your MySQL query statement below
SELECT f.employee_id, f.department_id
FROM Employee f
WHERE f.primary_flag = "Y" or f.employee_id in (SELECT e.employee_id
                                                FROM Employee e
                                                GROUP BY e.employee_id
                                                HAVING COUNT(e.employee_id) = 1)