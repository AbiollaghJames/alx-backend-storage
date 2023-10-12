-- script that lists all bands with Glam rock style,
-- ranked by their longevity
-- use of COALESE

SELECT band_name, COALESCE(split, 2022) - formed as lifespan FROM metal_bands
WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;
