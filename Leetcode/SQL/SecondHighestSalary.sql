/*
Write a SQL query to get the second highest salary from the Employee table.
*/

SELECT MAX(Salary) as SecondHighestSalary
FROM Employee
WHERE Salary NOT IN
(
  SELECT MAX(Salary) FROM Employee
);


/*Extra SELECT statement to handle NULL case*/
SELECT
(
  SELECT t.Salary FROM
  (
    SELECT DISTINCT Salary,
    DENSE_RANK() OVER (ORDER BY Salary DESC) AS rnk
    FROM Employee
  ) t
  WHERE t.rnk = 2
)
AS SecondHighestSalary;
