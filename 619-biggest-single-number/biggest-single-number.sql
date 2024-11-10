# Write your MySQL query statement below
SELECT MAX(m.num) as num
FROM (
    SELECT m.num
    FROM MyNumbers m
    GROUP BY m.num
    HAVING COUNT(m.num) = 1
) as m

