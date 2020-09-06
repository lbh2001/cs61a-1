-- email: aunghtetpaing@berkeley.edu


-- You are a DVD rental shop owner.

-- To run your shop smoothly, you created some tables
-- related to your shop.
--      `DVD` table to keep track of basic information about the DVDs
--      `inventory` table to keep track of the inventory in the shop.
--          NOTE: the total can be greater than the sum of available and rented,
--          meaning that there can be some missing copies.
--      `july_rental` table to keep track of rental history of the month of july
--
-- This question is in 2 parts.
--
-- NOTE: The tests for this question are NOT comprehensive, as they only
-- refer to the data tables as shown below. We will be grading this question
-- manually.
--
-- NOTE: In all scheme/sql questions you can put a multi-line answer
-- in a blank


CREATE TABLE DVD AS
    SELECT "DVD a" AS name, "*****" AS qualitys, 2017 AS year UNION
    SELECT "DVD b" , "*" , 1988 UNION
    SELECT "DVD c" , "***" , 2010 UNION
    SELECT "DVD d" , "***" , 2018 UNION
    SELECT "DVD e" , "***" , 2020 UNION
    SELECT "DVD f" , "*****" , 2019;

CREATE TABLE inventory AS
    SELECT "DVD a" AS name, 1 AS available, 2 AS rented, 3 AS total UNION
    SELECT "DVD b" , 2 , 3 , 10 UNION
    SELECT "DVD c" , 4 , 1 , 9 UNION
    SELECT "DVD d" , 7 , 2 , 11 UNION
    SELECT "DVD f" , 0 , 12, 20;

CREATE TABLE july_rental AS
    SELECT "DVD c" AS name, 1 AS rented_date, 5 AS return_date UNION
    SELECT "DVD f" , 4 , 10 UNION
    SELECT "DVD a" , 5 , 8 UNION
    SELECT "DVD b" , 5 , 9 UNION
    SELECT "DVD d" , 9 , 13 UNION
    SELECT "DVD f" , 10 , 15 UNION
    SELECT "DVD a" , 18, 26;

-- Part a : Complete the SQL statement below to select a one-column table
-- of DVD names whose release year is 2010 or later and have at least 1 copy
-- missing. Order your results by the number of missing copies, biggest to
-- smallest.
--
-- To run tests just for this part run
--      python3 ok -q a

CREATE TABLE parta AS
    SELECT a.name FROM inventory as a, DVD as b
    WHERE (total - available - rented) > 0
      AND a.name = b.name AND b.year >= 2010
    ORDER BY (total - available - rented) DESC;

-- Part b : We are interested in seeing how renting behavior correlates with
--      quality.
--
-- Complete the SQL statement below to create a two-column table that shows
-- how many DVDs per star quality have been rented out for a period of more
-- than 3 days.
--
-- For example, if a DVD was rented out on july 3 and returned on july 6,
-- that would not count as being rented out for more than 3 days, but if it
-- was returned on july 7 that would count as more than 3 days.
--
-- Each row should contain the star quality and number of DVDs. Only include quality
-- categories that have at least 2 DVDs satisfying the condition.
--
-- To run tests just for this part run
--      python3 ok -q b

CREATE TABLE partb AS
    SELECT qualitys, count(*) from DVD AS a, july_rental as b
    WHERE b.return_date - b.rented_date > 3
      AND a.name = b.name
      GROUP BY qualitys
      HAVING COUNT(*) >= 2
    ;


-- ORIGINAL SKELETON FOLLOWS
-- select * from partb;

-- -- You are a DVD rental shop owner.

-- -- To run your shop smoothly, you created some tables
-- -- related to your shop.
-- --      `DVD` table to keep track of basic information about the DVDs
-- --      `inventory` table to keep track of the inventory in the shop.
-- --          NOTE: the total can be greater than the sum of available and rented,
-- --          meaning that there can be some missing copies.
-- --      `july_rental` table to keep track of rental history of the month of july
-- --
-- -- This question is in 2 parts.
-- --
-- -- NOTE: The tests for this question are NOT comprehensive, as they only
-- -- refer to the data tables as shown below. We will be grading this question
-- -- manually.
-- --
-- -- NOTE: In all scheme/sql questions you can put a multi-line answer
-- -- in a blank


-- CREATE TABLE DVD AS
--     SELECT "DVD a" AS name, "*****" AS qualitys, 2017 AS year UNION
--     SELECT "DVD b" , "*" , 1988 UNION
--     SELECT "DVD c" , "***" , 2010 UNION
--     SELECT "DVD d" , "***" , 2018 UNION
--     SELECT "DVD e" , "***" , 2020 UNION
--     SELECT "DVD f" , "*****" , 2019;

-- CREATE TABLE inventory AS
--     SELECT "DVD a" AS name, 1 AS available, 2 AS rented, 3 AS total UNION
--     SELECT "DVD b" , 2 , 3 , 10 UNION
--     SELECT "DVD c" , 4 , 1 , 9 UNION
--     SELECT "DVD d" , 7 , 2 , 11 UNION
--     SELECT "DVD f" , 0 , 12, 20;

-- CREATE TABLE july_rental AS
--     SELECT "DVD c" AS name, 1 AS rented_date, 5 AS return_date UNION
--     SELECT "DVD f" , 4 , 10 UNION
--     SELECT "DVD a" , 5 , 8 UNION
--     SELECT "DVD b" , 5 , 9 UNION
--     SELECT "DVD d" , 9 , 13 UNION
--     SELECT "DVD f" , 10 , 15 UNION
--     SELECT "DVD a" , 18, 26;

-- -- Part a : Complete the SQL statement below to select a one-column table
-- -- of DVD names whose release year is 2010 or later and have at least 1 copy
-- -- missing. Order your results by the number of missing copies, biggest to
-- -- smallest.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q a

-- CREATE TABLE parta AS
--     SELECT "replace this;";

-- -- Part b : We are interested in seeing how renting behavior correlates with
-- --      quality.
-- --
-- -- Complete the SQL statement below to create a two-column table that shows
-- -- how many DVDs per star quality have been rented out for a period of more
-- -- than 3 days.
-- --
-- -- For example, if a DVD was rented out on july 3 and returned on july 6,
-- -- that would not count as being rented out for more than 3 days, but if it
-- -- was returned on july 7 that would count as more than 3 days.
-- --
-- -- Each row should contain the star quality and number of DVDs. Only include quality
-- -- categories that have at least 2 DVDs satisfying the condition.
-- --
-- -- To run tests just for this part run
-- --      python3 ok -q b

-- CREATE TABLE partb AS
--     SELECT "replace this;";
