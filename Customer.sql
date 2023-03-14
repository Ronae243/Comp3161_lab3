-- Create Database
CREATE DATABASE IF NOT EXISTS uwi3;


-- Create Table
USE uwi3;
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Gender VARCHAR(10),
    Age INT,
    Annual_Income INT,
    Spending_Score INT,
    Profession VARCHAR(50),
    Work_Experience INT,
    Family_Size INT
);

