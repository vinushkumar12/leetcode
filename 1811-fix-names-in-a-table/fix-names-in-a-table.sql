# Write your MySQL query statement below
SELECT u.user_id, CONCAT(LEFT(UPPER(u.name),1), LOWER(SUBSTR(LOWER(u.name),2))) as name
FROM Users u
ORDER BY u.user_id