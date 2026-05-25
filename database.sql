CREATE DATABASE matrimony;

USE matrimony;

CREATE TABLE profiles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(20),
    district VARCHAR(100),
    education VARCHAR(100),
    phone VARCHAR(20)
);