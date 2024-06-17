-- creates a table called first_table in the database
-- the table will have an ID of type INT
-- and a name with a possible 256 characters.
-- if the table already exists it wont fail

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
