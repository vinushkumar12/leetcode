# Write your MySQL query statement below
SELECT b.employee_id, b.name, COUNT(b.name) as reports_count, ROUND(AVG(e.age)) as average_age
FROM Employees e CROSS JOIN Employees b
WHERE e.reports_to = b.employee_id
GROUP BY b.employee_id
ORDER BY employee_id ASC