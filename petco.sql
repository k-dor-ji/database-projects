CREATE DATABASE petco;
USE petco;

CREATE TABLE EMPLOYEE(
   middleinitial VARCHAR(1),
   firstname VARCHAR(20),
   lastname VARCHAR(20),
   payrate INT,
   salary INT,
   role VARCHAR(20),
   employee_ID VARCHAR(20),
   PRIMARY KEY (employee_ID)
);

CREATE TABLE PETS(
   name VARCHAR(20),
   breed VARCHAR(20),
   dob DATE,
   pet_id VARCHAR(20),
   employee_ID VARCHAR(20),
   order_ID INT, -- Added order_ID column
   PRIMARY KEY (pet_id),
   FOREIGN KEY (employee_ID) REFERENCES EMPLOYEE(employee_ID),
   FOREIGN KEY (order_ID) REFERENCES CUSTOMERS(order_ID)
);

CREATE TABLE PRODUCTS(
   price INT,
   idNumber INT,
   expirationDate DATE,
   PRIMARY KEY (idNumber)
);

CREATE TABLE DEPARTMENT(
   deptName VARCHAR(20),
   dept_ID INT,
   PRIMARY KEY (dept_ID)
);

CREATE TABLE CUSTOMERS(
   middleInitial VARCHAR(1),
   firstname VARCHAR(20),
   lastname VARCHAR(20),
   order_ID INT,
   customer_ID INT,
   contactInfo VARCHAR(10),
   membership TINYINT,
   PRIMARY KEY(customer_ID)
);
