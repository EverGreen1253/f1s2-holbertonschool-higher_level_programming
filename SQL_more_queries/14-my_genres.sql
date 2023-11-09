-- get the genres that Dexter is classified under
SELECT DISTINCT (name) 
FROM tv_shows s 
INNER JOIN tv_show_genres sg ON s.id = sg.genre_id 
INNER JOIN tv_genres g ON sg.genre_id = g.id
WHERE s.title = "Dexter";