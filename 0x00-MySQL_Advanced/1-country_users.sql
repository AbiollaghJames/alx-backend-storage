-- SQL script to create table if not exists
-- country column must have default value as US

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country varchar(2) NOT NULL DEFAULT 'US',

	-- id as the primary key
	PRIMARY KEY (id)
);
