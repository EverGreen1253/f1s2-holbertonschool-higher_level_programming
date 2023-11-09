-- gets list of ALL show titles with genre ids (where available)
SELECT title, genre_id FROM tv_shows s
LEFT JOIN tv_show_genres sg ON s.id = sg.show_id
ORDER BY title ASC, genre_id ASC;