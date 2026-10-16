CREATE DATABASE Funct;

CREATE TABLE employee_details(
emp_id INT,
emp_name VARCHAR(50),
email VARCHAR(100),
salary DECIMAL(10,2),
joining_date DATE,
city VARCHAR(50)
);

INSERT INTO employee_details VALUES
(1,'  ram ','RAM@GMAIL.COM',10000.50,'2024-01-15','chennai'),
(2,'Priya','priya@gmail.com',25000.75,'2023-06-10','CHENNAI'),
(3,'KAVIN','KAVIN@GMAIL.COM',18000.00,'2022-12-01','Coimbatore'),
(4,'meena',NULL,22000.00,'2021-08-15','coimbatore'),
(5,'John','john@gmail.com',30000.00,'2020-05-20','MUMBAI');


SELECT * FROM employee_details;
#Remove unwanted spaces
SELECT emp_name, TRIM(emp_name) FROM employee_details;

#Convert all cities to uppercase
select emp_name, UPPER(emp_name) AS UPPER_NAME from employee_details;

#Store all emails in lowercase
SELECT email, lower(email) AS Lower_Case From employee_details;




#Validate name length
SELECT emp_name, length(emp_name) AS Length_Emp From employee_details;

#Q1HR wants employee names without leading or trailing spaces.
SELECT  emp_name, trim(emp_name) AS Trim_Space From employee_details;

#Q2Generate all emails in lowercase format.
SELECT email, lower(email) AS Lower_Email From employee_details;

#Q3Find employees whose names exceed 5 characters.
SELECT emp_name, length(emp_name)>5 AS Length_Emp From employee_details;

#Q4Generate joining dates in DD-MM-YYYY format.
SELECT date_format(joining_date, "%d-%m-%y") AS Date_Format From employee_details; 

#Q5Display current system date and time.
SELECT NOW();

#Round employee salaries to nearest whole number.
SELECT salary, ROUND(salary) AS Round_Salary FROM employee_details;

#Display highest salary.
Select Max(salary) From employee_details;

#Display average salary.
Select avg(salary) from employee_details;





