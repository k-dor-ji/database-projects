import sqlite3

# Connect to SQLite database (it will create it if it doesn't exist)
conn = sqlite3.connect('petco.db')
cursor = conn.cursor()

# SQL commands to create tables
cursor.executescript('''
CREATE TABLE IF NOT EXISTS EMPLOYEE(
   middleinitial VARCHAR(1),
   firstname VARCHAR(20),
   lastname VARCHAR(20),
   payrate INT,
   salary INT,
   role VARCHAR(20),
   employee_ID VARCHAR(20) PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS PETS(
   name VARCHAR(20),
   breed VARCHAR(20),
   dob DATE,
   pet_id VARCHAR(20) PRIMARY KEY,
   employee_ID VARCHAR(20),
   order_ID INT,
   FOREIGN KEY (employee_ID) REFERENCES EMPLOYEE(employee_ID)
);

CREATE TABLE IF NOT EXISTS PRODUCTS(
   price INT,
   idNumber INT PRIMARY KEY,
   expirationDate DATE
);

CREATE TABLE IF NOT EXISTS DEPARTMENT(
   deptName VARCHAR(20),
   dept_ID INT PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS CUSTOMERS(
   middleInitial VARCHAR(1),
   firstname VARCHAR(20),
   lastname VARCHAR(20),
   order_ID INT,
   customer_ID INT PRIMARY KEY,
   contactInfo VARCHAR(10),
   membership TINYINT
);
''')

# Commit and close the connection
conn.commit()
conn.close()
