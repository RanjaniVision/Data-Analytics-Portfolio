CREATE DATABASE EcommDB;

USE Ecommdb;



CREATE TABLE Customer_Data(
customer_id INT AUTO_INCREMENT PRIMARY KEY,
customer_name VARCHAR(100),
age INT,
gender VARCHAR(50),
city VARCHAR(50));

INSERT INTO Customer_Data(customer_name,age,gender,city)
VALUES
("Arjun",28,"Male","Chennai"),
("Priya",31,"Female","Coimbatore"),
("Rahul",26,"Male","Madurai"),
("Sneha",24,"Female","Salem"),
("Kavin",35,"Male","Trichy");


CREATE TABLE Product_Data(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(100),
price INT);

INSERT INTO Product_Data(product_id,product_name,category,price)
VALUES
(101,"Laptop","Electronics",55000),
(102,"Mobile","Electronics",22000),
(103,"Shoes","Fashion",2500),
(104,"Watch","Accessories",3200),
(105,"Chair","Furniture",4500);



CREATE TABLE Orders_Data(
order_id INT PRIMARY KEY,
customer_id INT,
product_id INT,
order_Date Date,
total_amount INT,

FOREIGN KEY (customer_id) REFERENCES Customer_Data (customer_id),
FOREIGN KEY (product_id) REFERENCES Product_Data (product_id)
);

INSERT INTO Orders_Data(order_id,customer_id,product_id,order_Date,total_amount)
VALUES
(1001,1,101,"2026-05-10",55000),
(1002,2,102,"2026-05-11",2500),
(1003,3,103,"2026-05-12",22000),
(1004,4,104,"2026-05-13",3200),
(1005,5,105,"2026-05-14",4500);


