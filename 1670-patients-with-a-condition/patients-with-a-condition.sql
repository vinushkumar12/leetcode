# Write your MySQL query statement below
SELECT *
FROM Patients p
WHERE p.conditions LIKE 'DIAB1%' or p.conditions LIKE '% DIAB1%'