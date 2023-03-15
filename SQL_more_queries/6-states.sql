-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT PRIMARY KEY UNIQUE NOT NULL AUTO-INCREMENT,
	name VARACHAR(256) NOT NULL
);
