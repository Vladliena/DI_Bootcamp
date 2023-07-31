-- CREATE TABLE FirstTab (
--      id integer, 
--      name VARCHAR(10)
-- )

-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar')

-- SELECT * FROM FirstTab

-- CREATE TABLE SecondTab (
--     id integer 
-- )

-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL)


-- SELECT * FROM SecondTab


-- Q1 What will be the OUTPUT of the following statement? - It will be 0 because we are doing NOT IN in NOTHING
-- SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )

-- Q2 What will be the OUTPUT of the following statement? It will be 2 ( counted: 6 'Sharlee' and 7, 'Krish' )
--  SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- Q3 What will be the OUTPUT of the following statement? It will be 0 because it cant compare between 2 id with NOT IN
--  SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

-- Q4  What will be the OUTPUT of the following statement? It gives us 2 ( counted: 6 'Sharlee' and 7, 'Krish' )
--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )

