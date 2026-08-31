# Write your MySQL query statement below
SELECT a.employee_id ,a.name,COUNT(b.employee_id) as reports_count,ROUND(AVG(b.age))as average_age
FROM Employees as a
JOIN Employees as b
ON a.employee_id=b.reports_to
GROUP BY a.employee_id,a.name
ORDER BY a.employee_id
