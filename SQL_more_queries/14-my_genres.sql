-- get the genres that Dexter is classified under
SELECT DISTINCT (name) 
FROM tv_shows s 
LEFT JOIN tv_show_genres sg ON s.id = sg.genre_id 
LEFT JOIN tv_genres g ON sg.genre_id = g.id
WHERE s.title = "Dexter";