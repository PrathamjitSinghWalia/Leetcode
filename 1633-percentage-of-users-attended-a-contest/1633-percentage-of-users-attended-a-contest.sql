# Write your MySQL query statement below
SELECT contest_id,
       ROUND(
           COUNT(b.user_id) * 100.0 / (SELECT COUNT(*) FROM Users),
           2
       ) AS percentage
FROM Users AS a
JOIN Register AS b
ON a.user_id = b.user_id
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;