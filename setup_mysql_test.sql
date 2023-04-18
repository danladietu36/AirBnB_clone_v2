-- script that prepares a MySQL server for the project
-- create a DATABASE with the name hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- create a new user with name hbnb_test and password hbnb_test_pwd
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- grant all PRIVILEGES on hbnb_test_db to user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
-- grant SELECT to user on performance_schema database
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
