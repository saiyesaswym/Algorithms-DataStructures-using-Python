
/*USING WINDOW FUNCTION*/

SELECT player_id, event_date,
SUM(games_played) OVER(PARTITION BY player_id ORDER BY event_date) as games_played_so_far
FROM
Activity;


/*USING SELF JOIN*/

SELECT t2.player_id, t2.event_date, sum(t1.games_played) as games_played_so_far
FROM activity t1, activity t2
WHERE t1.player_id = t2.player_id
AND t1.event_date <=t2.event_date
GROUP BY t2.player_id, t2.event_date;
