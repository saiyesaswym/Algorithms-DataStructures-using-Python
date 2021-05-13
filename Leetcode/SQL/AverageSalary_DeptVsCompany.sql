
/*Write a query to display the comparison result (higher/lower/same) of the average salary of employees in a department to the company's average salary.*/

WITH dept_avg AS
(
    SELECT LEFT(pay_date,7) as pay_month,
    e.department_id,
    AVG(s.amount) as dept_avg
    FROM salary s
    JOIN
    employee e
    ON s.employee_id = e.employee_id
    GROUP BY LEFT(pay_date,7), department_id
)
, comp_avg AS
(
    SELECT LEFT(pay_date,7) as pay_month,
    AVG(amount) as total_avg
    FROM Salary
    GROUP BY LEFT(pay_date,7)
)
SELECT c1.pay_month, c1.department_id,
CASE WHEN c1.dept_avg>c2.total_avg THEN 'higher'
WHEN c1.dept_avg<c2.total_avg THEN 'lower'
ELSE 'same' END AS comparison
FROM dept_avg c1
JOIN
comp_avg c2
ON c1.pay_month = c2.pay_month;
