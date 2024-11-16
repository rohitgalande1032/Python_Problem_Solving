--1......

-- Create player table to store name, age, and score 

CREATE TABLE Player (
    name VARCHAR(50),
    age INT,
    scrore INTEGER
)

--Frequently used Data types in SQL [INTEGER, FLOAT, VARCHAR(text), DATE, DATETIME, BOOLEAN]


-- INSERT clause used to insert new rows in table
-- Insert name, age and score of three players in the table

--2....

INSERT INTO Player(name, age, score) values ("Rohit", 35, 200),  ("Sachin", 40, 123), ("Virat", 34, 140)

--Notes
-- 1. No.of values that we're inserting must match with no.of columns specified in query
-- 2. We have to specify only existing tables in the database
-- 3. While adding data be careful with datatypes of input values and should be same as column datatypes


-- Retriving data
-- SELECT clause used to retrive data from table


--3....

-- Select specific column
SELECT name, age FROM Player

-- select all columns
SELECT * FROM Player

-- 4....

--WHERE Clause - specify condition that has to be satisfied for retrieving the data
 SELECT * FROM Player
 WHERE name = "Rohit"

 -- 5....

 -- UPDATE clause used to update the data of an existing table in databse. 
 -- We can update all the rows or specific rows as per requirements.

 -- Upadate all rows
 UPDATE Player
 SET score = 100

 -- Update specifi rows
 UPDATE Player
 SET score = 100
 WHERE NAME = "Rohit"


-- 6....

 --DELETE Clause used to delete existing records from table
 --DELETE all rows
 DELETE FROM Player

 --DELETE specific rows
 DELETE FROM Player 
 WHERE name = "Sachin"


 -- 7....
 --DROP table - DROP clause used to delete table from databse

 DROP TABLE Player

 -- 8....
 -- ALTER Table - Alter Clause used to add, delete, or modify columns in an existing table

 --===> ADD Column - Add a new column jersey_num of type integer to the player table
 ALTER TABLE Player
 ADD jersey_num INT

 --Note - Default value for newly added columns in the existing rows will be NULL

 --===> RENAME Column 
 ALTER TABLE Player
 RENAME COLUMN jursey_num TO jursey_number

 --====> DROP Column
 ALTER TABLE Player
 DROP COLUMN jursey_number

 --Note - DRPO COLUMN is not supported in some DBMS, including SQLite

