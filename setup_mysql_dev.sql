-- this script prepares a MySQL server for the project
-- create project development database with the name : hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creating a new user named hbnb dev with all privilieges on the hbnb_dev_db
-- with the password : hbnb_dev_pwd if it doesn't exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
--grants all privileges to new user
GRANT ALL PRIVILEGES ON hbnb_dev_db TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
--Grant sellect privilege for the user hbnb_dev in the de performance schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
