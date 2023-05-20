-- script that prepares a mysql server
-- dbname = hbnb_dev_db host=localhost
-- passwpord = hbnb_dev_pwd
-- privileges for hbnb_dev = all
-- privileges for hbnb_dev on hbnb_dev_db = select
-- id db already exists script should fail
CREATE SCHEMA IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';
CREATE PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performace_schema.* TO 'hbnb_dev'@'localhost';