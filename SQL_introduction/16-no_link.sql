-- list out all rows in second_table with names sorted by descending score
SELECT `score`, `name` FROM second_table WHERE `name` Is NOT NULL ORDER BY score DESC;