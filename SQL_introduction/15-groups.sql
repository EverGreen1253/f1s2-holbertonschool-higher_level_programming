-- the scores are grouped for display
SELECT `score`, COUNT(*) FROM second_table GROUP BY `score` ORDER BY score DESC;