# Write your MySQL query statement belo
SELECT r.contest_id as contest_id, ROUND((COUNT(u.user_id)/(SELECT COUNT(*) FROM Users) * 100),2) as percentage
FROM Users u join Register r
ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, r.contest_id ASC

