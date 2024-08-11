-- Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity

-- Requirements:

-- Import this table dump: metal_bands.sql.zip
-- Column names must be: band_name and lifespan (in years until 2022 - please use 2022 instead of YEAR(CURDATE()))
-- last year to calculate from is 2022
-- You should use attributes formed and split for computing the lifespan
-- Your script can be executed on any database
-- The CASE statement calculates the lifespan. If the split year is less than or equal to 2022, it uses split - formed. Otherwise, it uses 2022 - formed to handle bands that have not split yet or have split years beyond 2022.

SELECT band_name,
CASE
WHEN split <= 2022 THEN split - formed
ELSE 2022 - formed
END AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
