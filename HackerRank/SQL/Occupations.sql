
/*
Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation.
*/

SELECT [Doctor] as doctor,
[Professor] as professor,
[Singer] as singer,
[Actor] as actor
FROM
(
    SELECT Name, Occupation,
    row_number() over(partition by Occupation order by Name) as rnk
    FROM Occupations
)a
PIVOT
(
    MAX(Name)
    FOR [Occupation] IN ([Doctor],[Professor],[Singer],[Actor])
)b;
