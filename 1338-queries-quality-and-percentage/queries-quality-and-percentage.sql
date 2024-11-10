# Write your MySQL query statement below
SELECT temp.query_name, 
    ROUND(AVG(temp.rating/temp.position),2) as quality, 
    ROUND(SUM(CASE WHEN temp.rating < 3 THEN 1 ELSE 0 END)/COUNT(temp.query_name) * 100,2) as poor_query_percentage
FROM (SELECT DISTINCT * FROM Queries) as temp
WHERE temp.query_name IS NOT NULL
GROUP BY temp.query_name

