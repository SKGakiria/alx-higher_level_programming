-- Script creating the table unique_id on the MySQL server
CREATE TABLE IF NOT EXISTS db_name.unique_id (
id INT DEFAULT 1 UNIQUE,
name VARCHAR(256));
