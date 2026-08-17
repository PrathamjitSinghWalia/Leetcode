# Write your MySQL query statement below
SELECT firstName ,lastName,city,state
FROM PERSON as a 
LEFT JOIN Address as b
ON a.personId=b.personId;
