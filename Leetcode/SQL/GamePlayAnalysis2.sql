
/*Write a SQL query that reports the device that is first logged in for each player.*/

SELECT player_id, device_id FROM
(
  SELECT player_id, device_id,
  dense_rank() over(partition by player_id order by event_date) as rnk
  FROM Activity
)a
WHERE rnk=1;
