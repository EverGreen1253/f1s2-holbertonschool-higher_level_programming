-- get all films under genre Comedy
SELECT title 
FROM tv_genres g 
INNER JOIN tv_show_genres sg ON g.id = sg.genre_id 
INNER JOIN tv_shows s ON sg.show_id = s.id 
WHERE name = "Comedy";