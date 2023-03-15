-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT PRIMARY KEY UNIQUE NOT NULL AUTO-INCREMENT,
	state_id INT FOREIGN KEY REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL
);
