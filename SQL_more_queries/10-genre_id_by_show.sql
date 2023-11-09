-- gets list of show titles with their genre ids
SELECT title, genre_id FROM tv_shows s
INNER JOIN tv_show_genres sg ON s.id = sg.show_id
ORDER BY title ASC, genre_id ASC;