-- the scores are grouped for display
SELECT `score`, COUNT(*) as number FROM second_table GROUP BY `score` ORDER BY score DESC;