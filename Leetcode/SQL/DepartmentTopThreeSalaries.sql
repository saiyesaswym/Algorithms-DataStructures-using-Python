
/*
Write a SQL query to find employees who earn the top three salaries in each of the department. 
*/

WITH cte_tab as(
  SELECT *, dense_rank() over(partition by DepartmentId Order by Salary desc) as rnk
  FROM Employee
)
SELECT d.Name as Department, t.Name as Employee, t.Salary
FROM cte_tab t
JOIN
Department d
ON t.DepartmentId = d.Id
WHERE rnk<=3;
