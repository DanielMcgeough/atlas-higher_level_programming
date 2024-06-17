-- lists all records of the second table
-- doesnt list rows witho a name value
-- listed in DESC order

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
