-- gets list of show titles with no genre ids
SELECT title, genre_id FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
WHERE genre_id IS NULL
ORDER BY title ASC, genre_id ASC;