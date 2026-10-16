CREATE DATABASE Company_db;

USE Company_db;


CREATE TABLE Employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department VARCHAR(50),
    salary DECIMAL(10,2),
    joining_date DATE,
    bonus DECIMAL(10,2),
    phone_number VARCHAR(20)
);

INSERT INTO Employees VALUES
(101, ' Arun Kumar ', 'HR', 45000.75, '2022-01-15', 5000, '9876543210'),
(102, 'Priya Sharma', 'IT', 65000.50, '2021-07-10', NULL, '9123456780'),
(103, 'Rahul Verma', 'Finance', 55000.20, '2020-03-22', 7000, NULL),
(104, 'Sneha Iyer', 'IT', 72000.99, '2019-11-01', 8000, '9988776655'),
(105, 'Kiran Das', 'Sales', 39000.40, '2023-05-18', NULL, NULL);

SELECT UPPER(employee_name) AS 'UPPER CASE NAME' 
FROM Employees;

SELECT employee_name, salary 
FROM employees
WHERE salary > 50000;

SELECT * FROM Employees;

SHOW TABLES;



Batch 1 - CDPDAI