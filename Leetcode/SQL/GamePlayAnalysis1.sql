
/*Write an SQL query that reports the first login date for each player.*/

SELECT player_id,
MIN(event_date) as first_login
FROM Activity
GROUP BY player_id;


/*Using dense_rank*/

WITH cte_tab AS
(
    SELECT *,
    dense_rank() over(partition by player_id order by event_date) as rnk
    FROM Activity
)
SELECT player_id, event_date as first_login
FROM cte_tab WHERE rnk=1;
