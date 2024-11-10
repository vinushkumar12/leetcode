# Write your MySQL query statement below
SELECT t.x, t.y, t.z, CASE
                        WHEN t.x <= 0 or t.y <= 0 or t.z <= 0 THEN "No"
                        WHEN GREATEST(t.x,t.y,t.z) = t.x and t.y + t.z > t.x THEN "Yes"
                        WHEN GREATEST(t.x,t.y,t.z) = t.y and t.x + t.z > t.y THEN "Yes"
                        WHEN GREATEST(t.x,t.y,t.z) = t.z and t.x + t.y > t.z THEN "Yes"
                        ELSE "No"
                      END as triangle
FROM Triangle t