-- Script computing the score average of all records in the table second_table of the database hbtn_0c_0 in the MySQL server
SELECT SUM(`score`) / COUNT(*) AS "average" FROM second_table;
