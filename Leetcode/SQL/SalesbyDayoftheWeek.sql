
/*
Write an SQL query to report how many units in each category have been ordered on each day of the week.
*/

/*Using PIVOT keyword*/

SELECT item_category AS CATEGORY,
ISNULL([Monday],0) as MONDAY,
ISNULL([Tuesday],0) as TUESDAY,
ISNULL([Wednesday],0) as WEDNESDAY,
ISNULL([Thursday],0) as THURSDAY,
ISNULL([Friday],0) as FRIDAY,
ISNULL([Saturday],0) as SATURDAY,
ISNULL([Sunday],0) as SUNDAY
FROM
(
    SELECT i.item_category,
    DATENAME(dw, o.order_date) as day_of_week,
    ISNULL(o.quantity,0) as qty
    FROM Orders o
    RIGHT JOIN
    Items i
    ON o.item_id = i.item_id
) a
PIVOT
(
    SUM(qty)
    FOR [day_of_week] IN ([Monday],[Tuesday],[Wednesday],[Thursday],[Friday],[Saturday],[Sunday])
) b
ORDER BY item_category;


/*Using CASE WHEN THEN*/

WITH cte_tab AS(
  SELECT *,
  DATENAME(dw, order_date) as day_of_week
  FROM Orders
)
SELECT i.item_category as CATEGORY,
SUM(CASE WHEN c.day_of_week='Monday' THEN c.quantity ELSE 0 END) AS MONDAY,
SUM(CASE WHEN c.day_of_week='Tuesday' THEN c.quantity ELSE 0 END) AS TUESDAY,
SUM(CASE WHEN c.day_of_week='Wednesday' THEN c.quantity ELSE 0 END) AS WEDNESDAY,
SUM(CASE WHEN c.day_of_week='Thursday' THEN c.quantity ELSE 0 END) AS THURSDAY,
SUM(CASE WHEN c.day_of_week='Friday' THEN c.quantity ELSE 0 END) AS FRIDAY,
SUM(CASE WHEN c.day_of_week='Saturday' THEN c.quantity ELSE 0 END) AS SATURDAY,
SUM(CASE WHEN c.day_of_week='Sunday' THEN c.quantity ELSE 0 END) AS SUNDAY
FROM items i
LEFT JOIN
cte_tab c
ON i.item_id = c.item_id
GROUP BY item_category;
