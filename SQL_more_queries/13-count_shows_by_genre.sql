-- list out the gneres and the number of shows that are tagged with them
SELECT name AS genre, COUNT(show_id) AS number_of_shows 
FROM tv_genres g 
LEFT JOIN tv_show_genres sg ON g.id = sg.genre_id 
GROUP BY name;

-- SELECT name, number_of_shows 
-- FROM tv_genres LEFT JOIN (
--     SELECT genre_id AS genre, COUNT(show_id) AS number_of_shows
--     FROM tv_show_genres
--     GROUP BY genre_id
-- ) x 
-- ON tv_genres.id = x.genre;