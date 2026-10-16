CREATE DATABASE emp_master_db;

CREATE TABLE employee_master(
emp_id INT,
emp_name VARCHAR(50),
email VARCHAR(100),
mobile VARCHAR(20),
department VARCHAR(30),
city VARCHAR(50)
);

INSERT INTO employee_master VALUES
(1, 'ram kumar', 'RAM@GMAIL.COM', '9876543210', 'IT', 'chennai'),
(2, 'Priya Sharma', 'PRIYA@YAHOO.COM', '9876543211', 'HR', 'CHENNAI'),
(3, 'kavin raj', 'kavin@gmail.com', '9876543212', 'IT', 'Coimbatore'),
(4, 'John Peter', NULL, '9876543213', 'Finance', 'MUMBAI'),
(5, 'MEENA', 'MEENA@GMAIL.COM', '9876543214', 'HR', 'coimbatore');

SELECT * FROM employee_master;


USE emp_master_db;

#1.HR Data Cleanup Requests, DC-01: Generate employee names without leading or trailing spaces.
SELECT emp_name,
trim(emp_name) AS Trim_Name 
FROM employee_master;

#2.Standardize all employee names into uppercase format.
SELECT emp_name,
upper(emp_name) AS Upper_Case_Name
FROM employee_master;

#3.Standardize all email addresses into lowercase format.
SELECT email,
lower(email) AS Lower_Case 
FROM employee_master;

#4.Generate a report showing the number of characters in each employee name.
SELECT emp_name,
length(emp_name) AS Length_Chara
FROM employee_master;

#5.Identify employees whose names exceed 10 characters.
SELECT emp_name,
length(emp_name)>10 AS Lengh_10name
FROM 
employee_master; 

#6.Generate a list of employees whose email address belongs to Gmail.
SELECT emp_name,email
FROM employee_master
WHERE email 
LIKE '%@gmail.com';


#7.Generate a list of employees whose names begin with the letter M.
SELECT emp_name
FROM employee_master
where emp_name LIKE 'M%';

#8.Display the first 5 characters of every employee name.
SELECT emp_name,
LEFT(emp_name, 5) AS Short_Name
FROM employee_master;

#9.DC-09: Display the last 4 digits of each employees mobile number.
SELECT mobile,
LEFT(mobile, 4) AS Digit_Mobile
FROM employee_master;

#10.Generate a report showing employee name and city in the format EMPLOYEE_NAME-CITY
SELECT CONCAT(emp_name, '-', city) 
AS EMPLOYEE_NAME_CITY 
FROM employee_master;

#11.Generate an output where the city name CHENNAI is displayed as CHENNAI HQ.

SELECT emp_name,
       CASE
           WHEN UPPER(city) = 'CHENNAI' THEN 'CHENNAI HQ'
           ELSE city
       END AS city_name
FROM employee_master;

#12.Generate employee email addresses. If an email address is missing, display Email Not Available.
SELECT emp_name,
       ifnull(email, 'Email Not Available') AS email_address
FROM employee_master;
#(coalesce its used for check non-null, ifnull is return value,replace value)

#13.Generate a unique list of cities available in the employee database.
SELECT
DISTINCT city
AS Unique_City
FROM employee_master;

#.DC-14: Identify employees whose email address is missing.
SELECT emp_name,email
FROM employee_master
WHERE email IS NULL;

#15.Generate a migration-ready employee report containing Employee Name, Email Address, Department, City, and Email Status.
SELECT
    emp_name AS 'Employee Name',
    email AS 'Email Address',
    department AS 'Department',
    city AS 'City',
    CASE
        WHEN email IS NULL THEN 'Inactive'
        ELSE 'Active'
    END AS 'Email Status'
FROM employee_master;

#DC-16: Generate employee initials from employee names. Example: Ram Kumar → RK.
SELECT emp_name,
       UPPER(
           CONCAT(
               LEFT(TRIM(emp_name),1),
               LEFT(SUBSTRING_INDEX(TRIM(emp_name),' ',-1),1)
           )
       ) AS Initials
FROM employee_master;

#Identify employees whose mobile number contains duplicate digits more than three times.

#Generate employee usernames using the first three letters of the employee name and last four digits of the mobile number.
SELECT emp_name,
       CONCAT(
           LEFT(TRIM(emp_name), 3),
           RIGHT(mobile, 4)
       ) AS Username
FROM employee_master;

# Generate a city-wise employee count report.
SELECT city,
       COUNT(*) AS Employee_Count
FROM employee_master
GROUP BY city;

#Generate a department-wise employee count report.
SELECT department,
       COUNT(*) AS Employee_Count
FROM employee_master
GROUP BY department;

SELECT * FROM employee_master;
