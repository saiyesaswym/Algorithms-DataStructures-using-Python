
/*
Given tables: Teams and Matches
Write an SQL query that selects the team_id, team_name and num_points of each team in the tournament after all described matches. 
*/

SELECT t.team_id,
t.team_name,
SUM(CASE WHEN t.team_id = m.host_team AND m.host_goals > m.guest_goals THEN 3
WHEN t.team_id = m.guest_team AND m.host_goals < m.guest_goals THEN 3
WHEN m.host_goals = m.guest_goals THEN 1 ELSE 0
END) AS num_points
from Teams t
left join Matches m
on t.team_id = m.host_team
or t.team_id = m.guest_team
GROUP BY t.team_id, t.team_name
ORDER BY num_points desc, team_id;
