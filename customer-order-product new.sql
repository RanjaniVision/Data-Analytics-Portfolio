CREATE DATABASE Cust_db;

USE Cust_db;

CREATE TABLE Customer(
Customer_id INT AUTO_INCREMENT PRIMARY KEY,
Cust_Name VARCHAR(100));

INSERT INTO Customer(Cust_Name)
VALUES
('Arjun'),
('Priya'),
('Kavin'),
('Meena');


#ORDER TABLE
CREATE TABLE Orders (
    Order_id INT PRIMARY KEY,
    Customer_id INT,
    Order_Date DATE,
    FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
);

INSERT INTO Orders (Order_id,Customer_id,Order_Date)
VALUES
(101, 1, '2026-01-10'),
(102, 1, '2026-01-15'),
(103, 2, '2026-01-18'),
(104, 5, '2026-01-20');
INSERT INTO Customer VALUES (5, '2026-01-24');


#PRODUCT TABLE
CREATE TABLE Product(
Product_Id INT PRIMARY KEY,
Product VARCHAR(100));

INSERT INTO Product(Product_Id,Product)
VALUES
(201, 'Laptop'),
(202, 'Mobile'),
(203, 'Mouse');



#ORDER DETAILS
CREATE TABLE Orders_details(
Order_id INT,
Product_Id INT,
Quantity INT,
FOREIGN KEY (Order_id) REFERENCES Orders(Order_id),
FOREIGN KEY (Product_Id) REFERENCES Product(Product_Id));

INSERT INTO Orders_details(Order_id,Product_Id,Quantity)
VALUES
(101, 201, 1),
(101, 203, 2),
(102, 202, 1),
(103, 203, 3);

#1.Display customer names with their order IDs. 
SELECT Customer.Cust_Name, Orders.Order_id
FROM Customer
JOIN Orders
ON Customer.Customer_id = Orders.Customer_id;

#2.Show customer names and order dates. 
SELECT Customer.Cust_Name, Orders.Order_Date
FROM Customer
JOIN Orders
ON Customer.Customer_id = Orders.Customer_id;

#.Display all customers who placed orders. 
SELECT DISTINCT Customer.Cust_Name
FROM Customer
JOIN Orders
ON Customer.Customer_id = Orders.Customer_id;

#4.Show order ID and customer name for each order. 
SELECT Orders.Order_id, Customer.Cust_Name
FROM Orders
JOIN Customer
ON Orders.Customer_id = Customer.Customer_id;

#.Show product names purchased in each order. 
SELECT Orders_details.Order_id, Product.Product
FROM Orders_details
JOIN Product
ON Orders_details.Product_Id = Product.Product_Id;

#6.Display all customers including customers who never placed orders.
SELECT Customer.Cust_Name, Orders.Order_id
FROM Customer
LEFT JOIN Orders
ON Customer.Customer_id = Orders.Customer_id;

#7.Find customers without orders. 

SELECT Customer.Cust_Name
FROM Customer
LEFT JOIN Orders
ON Customer.Customer_id = Orders.Customer_id
WHERE Orders.Order_id IS NULL;

#8.Show all customers and their order dates if available. 
SELECT Customer.Cust_Name, Orders.Order_Date
FROM Customer
LEFT JOIN Orders
ON Customer.Customer_id = Orders.Customer_id;

#9.Display all products even if never ordered. 
SELECT Product.Product, Orders_details.Order_id
FROM Product
LEFT JOIN Orders_details
ON Product.Product_Id = Orders_details.Product_Id;

#10.Find products that were never purchased. 
SELECT Product.Product
FROM Product
LEFT JOIN Orders_details
ON Product.Product_Id = Orders_details.Product_Id
WHERE Orders_details.Order_id IS NULL;

#11.Display all orders including orders with invalid customer IDs. 
SELECT Orders.Order_id, Customer.Cust_Name
FROM Customer
RIGHT JOIN Orders
ON Customer.Customer_id = Orders.Customer_id;

#12.12.Show all order IDs and customer names.Even unmatched orders must appear.
SELECT Orders.Order_id, Customer.Cust_Name
FROM Orders
LEFT JOIN Customer
ON Orders.Customer_id = Customer.Customer_id;

#13.Find orders that do not have valid customers. 
SELECT Orders.Order_id
FROM Orders
LEFT JOIN Customer
ON Orders.Customer_id = Customer.Customer_id
WHERE Customer.Customer_id IS NULL;