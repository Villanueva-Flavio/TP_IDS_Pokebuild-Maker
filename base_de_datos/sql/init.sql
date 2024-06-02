CREATE DATABASE IF NOT EXISTS pokebuildmaker;
USE pokebuildmaker;

CREATE TABLE USER (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    profile_picture VARCHAR(255) NOT NULL
);

CREATE TABLE POKEMON (
    id INT AUTO_INCREMENT PRIMARY KEY,
    podekex_id INT(4) NOT NULL,
    level INT(3) NOT NULL,
    name VARCHAR(12),
    ability_1 VARCHAR(30) NOT NULL,
    ability_2 VARCHAR(30),
    ability_3 VARCHAR(30),
    ability_4 VARCHAR(30),
    owner_id INT NOT NULL,
    CONSTRAINT fk_owner FOREIGN KEY (owner_id) REFERENCES USER(id)
);
