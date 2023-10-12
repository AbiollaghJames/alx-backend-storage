-- script that ranks country origin of bands
-- order by num of fans
-- columns shown are origin and nb_fans

SELECT origin, SUM(fans) as nb_fans FROM metal_bands
GROUP BY origin ORDER BY nb_fans DESC;
