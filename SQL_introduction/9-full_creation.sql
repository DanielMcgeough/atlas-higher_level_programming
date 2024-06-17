-- create a talbe and add multiple rows to it
-- new rows will have id, name and score as fields

CREATE TABLE IF NOT EXISTS second_table (id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score)
VALUES (1, "John", 10),
(2, "Alex", 3),
(3, "Bob", 14).
(4, "George", 8);
