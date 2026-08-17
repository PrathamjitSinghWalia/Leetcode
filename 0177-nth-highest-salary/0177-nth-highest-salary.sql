CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
    RETURN (
        SELECT MAX(salary)
        FROM Employee e
        WHERE (
            SELECT COUNT(DISTINCT salary)
            FROM Employee e2
            WHERE e2.salary > e.salary
        ) = N - 1
    );
END