# CREATE DATABASE tide_type26_chaoxing;

USE tide_type26_chaoxing;

CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE container (
    id INT PRIMARY KEY AUTO_INCREMENT,
    cfg_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    note VARCHAR(512) NOT NULL
);

CREATE TABLE configuration (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    note VARCHAR(512) NOT NULL,
    path VARCHAR(255) NOT NULL
);