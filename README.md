# Discription
#### Instructor Database
1. Java-based GUI
   - The Java program is a GUI application using JavaFX for a University Information System. It allows users to retrieve and insert instructor information. The main features include querying instructors by ID, inserting new instructors, and handling errors with a clear layout. The code reads and writes data from/to text files, dynamically adapts to varying file sizes, and ensures a user-friendly interface.

2. Python-based GUI
   - The code defines a GUI application in Python using Tkinter for a University Information System. It features options to retrieve instructor or department information, clear the interface, or quit the program. The program reads data from text files, dynamically updates the GUI based on user input, and handles errors with appropriate messages.

#### Petco Database
- A relational database named "petco" with tables for EMPLOYEE, PETS, PRODUCTS, DEPARTMENT, and CUSTOMERS. It defines columns for employee, pet, product, department, and customer information, establishing relationships between tables using primary and foreign keys.

##### Employee
`Employee → Assists → Customers`
`Employee → Manages → Pets`
`Employee → Manages → Products`

The primary key for an employee class is the employee_id. That is because the employee_id is usually unique for each employee within the company. Thus, it makes the perfect primary key to retrieve unique tuples without returning duplicates from the table. The employee class is related to the customers class since employees are expected to assist customers with their questions. The employee class is also related to the pets class since the pet store requires employees to manage and service the pets according to the customer’s needs. Finally, the employee is related to the products class since employees are expected to take care of and sell their company products to potential customers.



##### Pets
Similar to the employee class, the primary key for the pets class is the pet_id. The pet_id is an id given by the employees to uniquely identify different pets and their orders. Therefore, it is a unique key which can display tuples which are not duplicated. The pet class also contains 2 foreign keys, the employee_id and the order_id. The employee_id acts to identify the specific employee assigned to complete the order, also known as the order_id.

##### Products
`Products → Managed → Employee`

The product class includes multiple keys within it. The keys aim to identify the product information closely, such as price, expiration date, and id number. Since the idnumber is a unique key that identifies a tuple from the products table without duplicate values, it is most appropriate to be assigned as the primary key for the table. This table does not have a foreign key but it does have a few relational connections with the employee table.

##### Department
`Departments → Assign → Employee`

The department class has few and straightforward keys. These include the department name and the department id, known as dept_id. Since the dept_id is uniquely assigned for each department, it is also the most suitable as the primary key for the table. The department class has one important relation with the employee class.

##### Customers
`Customers → Own → Pets`
`Customers → Buy → Products`

The customer class has the primary key customer_id since it is a unique key which returns non-duplicate tuples. The customers table includes the foreign key pet_id since customers own their pets and the orders that are associated with the pets are a part of the customers final order from the company and the employee. The customer has a relational connection with both the pets and products table.
