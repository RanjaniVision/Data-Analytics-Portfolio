CREATE DATABASE Hosproduct_tableproduct_tablepital_db;
use Hospital_db;

CREATE TABLE doctors(
doctors_id INT PRIMARY KEY AUTO_INCREMENT,
doctors_name VARCHAR(100),
specialization VARCHAR(100),
experience_year INT
);
product_table
INSERT INTO doctors
VALUES
(1,"Dr.Sharma","Cardiologist",12),
(2,"Dr.Mehta","Neurologist",8),
(3,"Dr.Ramesh","Orthopedic",15);


CREATE TABLE patient(
patient_id INT PRIMARY KEY,
patient_name VARCHAR(100),
patient_age INT,
gender VARCHAR(50));

INSERT INTO patient
VALUES
(101,"Anjali",45,"F"),
(102,"Rajesh",60,"M"),
(103,"Priya",30,"F"),
(104,"Sunil",55,"M");


CREATE TABLE appointments(
appointment_id INT PRIMARY KEY,
patient_id INT,
doctors_id INT,
appointment_date DATE,
appointment_status VARCHAR(50),

FOREIGN KEY (patient_id) REFERENCES patient(patient_id),
FOREIGN KEY (doctors_id) REFERENCES doctors(doctors_id)
);

INSERT INTO appointments
VALUES 
(201,101,1,"2023-06-01","Completed"),
(202,102,2,"2023-06-05","Pending"),
(203,103,1,"2023-06-07","Completed"),
(204,104,3,"2023-06-10","Pending");


CREATE TABLE treatment(
treatment_id INT PRIMARY KEY,
appointment_id INT,
treatment_details VARCHAR(100),
treatment_cost INT,

FOREIGN KEY(appointment_id) REFERENCES appointments(appointment_id)
);

INSERT INTO treatment
VALUES
(301,201,"Heart Checkup",7000),
(302,203,"Blood Pressure Test",1500),
(303,204,"Bone Fracture Care",9000);


#1. Display all doctors and their specializations.
SELECT doctors_name, specialization
FROM doctors;

#2. Show all patients older than 40 years.  
SELECT * FROM patient
WHERE patient_age > 40;

#3. List all appointments with status = "Pending". 
SELECT * FROM appointments
WHERE appointment_status="Pending";

#4. Display all patients in ascending order of their age.  
SELECT * FROM patient
ORDER BY patient_age;

#5. Show all treatments costing more than 5000.  
SELECT * FROM treatment
WHERE treatment_cost>5000;
 
 #6. Display the names of doctors who have more than  10 years of experience.
SELECT doctors_name
FROM doctors
WHERE experience_year > 10;
