import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class PetcoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Petco Database Management")
        self.root.configure(bg='black')

        self.selected_type = tk.StringVar(value="Employee")
        self.create_widgets()
        self.create_database()

    def create_database(self):
        conn = sqlite3.connect('petco.db')
        cursor = conn.cursor()
        # Create tables if they don't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS EMPLOYEE (
                middleinitial VARCHAR(1),
                firstname VARCHAR(20),
                lastname VARCHAR(20),
                payrate INT,
                salary INT,
                role VARCHAR(20),
                employee_ID VARCHAR(20) PRIMARY KEY
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS CUSTOMERS (
                middleInitial VARCHAR(1),
                firstname VARCHAR(20),
                lastname VARCHAR(20),
                order_ID INT,
                customer_ID INT PRIMARY KEY,
                contactInfo VARCHAR(10),
                membership TINYINT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS DEPARTMENT (
                deptName VARCHAR(20),
                dept_ID INT PRIMARY KEY
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS PETS (
                name VARCHAR(20),
                breed VARCHAR(20),
                dob DATE,
                pet_id VARCHAR(20) PRIMARY KEY,
                employee_ID VARCHAR(20),
                order_ID INT
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS PRODUCTS (
                price INT,
                idNumber INT PRIMARY KEY,
                expirationDate DATE
            )
        ''')
        conn.commit()
        conn.close()

    def create_widgets(self):
        # Selection dropdown
        self.lbl_select_type = tk.Label(self.root, text="Select Type to Add:", bg='black', fg='white')
        self.lbl_select_type.grid(row=0, column=0, padx=10, pady=5)

        self.dropdown = ttk.Combobox(self.root, textvariable=self.selected_type, values=["Employee", "Customer", "Department", "Pet", "Product"], state="readonly")
        self.dropdown.grid(row=0, column=1, padx=10, pady=5)
        self.dropdown.bind("<<ComboboxSelected>>", self.update_input_fields)

        self.input_frame = tk.Frame(self.root, bg='black')
        self.input_frame.grid(row=1, columnspan=2, padx=10, pady=5)

        self.lbl_search_key = tk.Label(self.root, text="Search by ID:", bg='black', fg='white')
        self.lbl_search_key.grid(row=2, column=0, padx=10, pady=5)
        self.entry_search_id = tk.Entry(self.root, bg='gray', fg='white')
        self.entry_search_id.grid(row=2, column=1, padx=10, pady=5)

        self.btn_search = tk.Button(self.root, text="Search", command=self.search_entry, bg='blue', fg='white')
        self.btn_search.grid(row=2, column=2, padx=10, pady=5)

        self.btn_add = tk.Button(self.root, text="Add", command=self.add_entry, bg='green', fg='white')
        self.btn_add.grid(row=3, columnspan=3, padx=10, pady=5)

        self.btn_back = tk.Button(self.root, text="Back", command=self.clear_inputs, bg='orange', fg='white')
        self.btn_back.grid(row=4, column=0, padx=10, pady=5)

        self.btn_quit = tk.Button(self.root, text="Quit", command=self.root.quit, bg='red', fg='white')
        self.btn_quit.grid(row=4, column=1, padx=10, pady=5)

        self.txt_output = tk.Text(self.root, height=10, width=50, bg='gray', fg='white')
        self.txt_output.grid(row=5, columnspan=3, padx=10, pady=5)

        self.update_input_fields()  # Initialize input fields based on the default selection

    def update_input_fields(self, event=None):
        # Clear previous input fields and search results
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.txt_output.delete(1.0, tk.END)  # Clear search results

        entry_type = self.selected_type.get()

        if entry_type == "Employee":
            self.create_employee_fields()
        elif entry_type == "Customer":
            self.create_customer_fields()
        elif entry_type == "Department":
            self.create_department_fields()
        elif entry_type == "Pet":
            self.create_pet_fields()
        elif entry_type == "Product":
            self.create_product_fields()

    def create_employee_fields(self):
        tk.Label(self.input_frame, text="Employee ID:", bg='black', fg='white').grid(row=0, column=0)
        self.entry_employee_id = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_employee_id.grid(row=0, column=1)

        tk.Label(self.input_frame, text="First Name:", bg='black', fg='white').grid(row=1, column=0)
        self.entry_first_name = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_first_name.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Last Name:", bg='black', fg='white').grid(row=2, column=0)
        self.entry_last_name = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_last_name.grid(row=2, column=1)

        tk.Label(self.input_frame, text="Pay Rate:", bg='black', fg='white').grid(row=3, column=0)
        self.entry_pay_rate = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_pay_rate.grid(row=3, column=1)

    def create_customer_fields(self):
        tk.Label(self.input_frame, text="Customer ID:", bg='black', fg='white').grid(row=0, column=0)
        self.entry_customer_id = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_customer_id.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Middle Initial:", bg='black', fg='white').grid(row=1, column=0)
        self.entry_cust_middle_initial = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_cust_middle_initial.grid(row=1, column=1)

        tk.Label(self.input_frame, text="First Name:", bg='black', fg='white').grid(row=2, column=0)
        self.entry_cust_first_name = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_cust_first_name.grid(row=2, column=1)

        tk.Label(self.input_frame, text="Last Name:", bg='black', fg='white').grid(row=3, column=0)
        self.entry_cust_last_name = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_cust_last_name.grid(row=3, column=1)

        tk.Label(self.input_frame, text="Contact Info:", bg='black', fg='white').grid(row=4, column=0)
        self.entry_contact_info = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_contact_info.grid(row=4, column=1)

        tk.Label(self.input_frame, text="Membership (1/0):", bg='black', fg='white').grid(row=5, column=0)
        self.entry_membership = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_membership.grid(row=5, column=1)

    def create_department_fields(self):
        tk.Label(self.input_frame, text="Department ID:", bg='black', fg='white').grid(row=0, column=0)
        self.entry_dept_id = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_dept_id.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Department Name:", bg='black', fg='white').grid(row=1, column=0)
        self.entry_dept_name = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_dept_name.grid(row=1, column=1)

    def create_pet_fields(self):
        tk.Label(self.input_frame, text="Pet ID:", bg='black', fg='white').grid(row=0, column=0)
        self.entry_pet_id = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_pet_id.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Pet Name:", bg='black', fg='white').grid(row=1, column=0)
        self.entry_pet_name = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_pet_name.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Breed:", bg='black', fg='white').grid(row=2, column=0)
        self.entry_breed = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_breed.grid(row=2, column=1)

    def create_product_fields(self):
        tk.Label(self.input_frame, text="Product ID:", bg='black', fg='white').grid(row=0, column=0)
        self.entry_product_id = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_product_id.grid(row=0, column=1)

        tk.Label(self.input_frame, text="Price:", bg='black', fg='white').grid(row=1, column=0)
        self.entry_product_price = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_product_price.grid(row=1, column=1)

        tk.Label(self.input_frame, text="Expiration Date:", bg='black', fg='white').grid(row=2, column=0)
        self.entry_expiration_date = tk.Entry(self.input_frame, bg='gray', fg='white')
        self.entry_expiration_date.grid(row=2, column=1)

    def add_entry(self):
        entry_type = self.selected_type.get()

        if entry_type == "Employee":
            self.add_employee()
        elif entry_type == "Customer":
            self.add_customer()
        elif entry_type == "Department":
            self.add_department()
        elif entry_type == "Pet":
            self.add_pet()
        elif entry_type == "Product":
            self.add_product()

    def add_employee(self):
        employee_id = self.entry_employee_id.get().strip()
        first_name = self.entry_first_name.get().strip()
        last_name = self.entry_last_name.get().strip()
        pay_rate = self.entry_pay_rate.get().strip()

        if not self.validate_input(employee_id, first_name, last_name, pay_rate):
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")
            return

        try:
            conn = sqlite3.connect('petco.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO EMPLOYEE (employee_ID, firstname, lastname, payrate)
                VALUES (?, ?, ?, ?)
            ''', (employee_id, first_name, last_name, int(pay_rate)))
            conn.commit()
            messagebox.showinfo("Success", "Employee added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Employee ID already exists.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def add_customer(self):
        customer_id = self.entry_customer_id.get().strip()
        middle_initial = self.entry_cust_middle_initial.get().strip()
        first_name = self.entry_cust_first_name.get().strip()
        last_name = self.entry_cust_last_name.get().strip()
        contact_info = self.entry_contact_info.get().strip()
        membership = self.entry_membership.get().strip()

        if not self.validate_input(customer_id, middle_initial, first_name, last_name, contact_info, membership):
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")
            return

        try:
            conn = sqlite3.connect('petco.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO CUSTOMERS (customer_ID, middleInitial, firstname, lastname, contactInfo, membership)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (customer_id, middle_initial, first_name, last_name, contact_info, int(membership)))
            conn.commit()
            messagebox.showinfo("Success", "Customer added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Customer ID already exists.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def add_department(self):
        dept_id = self.entry_dept_id.get().strip()
        dept_name = self.entry_dept_name.get().strip()

        if not self.validate_input(dept_id, dept_name):
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")
            return

        try:
            conn = sqlite3.connect('petco.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO DEPARTMENT (dept_ID, deptName)
                VALUES (?, ?)
            ''', (int(dept_id), dept_name))
            conn.commit()
            messagebox.showinfo("Success", "Department added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Department ID already exists.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def add_pet(self):
        pet_id = self.entry_pet_id.get().strip()
        pet_name = self.entry_pet_name.get().strip()
        breed = self.entry_breed.get().strip()

        if not self.validate_input(pet_id, pet_name, breed):
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")
            return

        try:
            conn = sqlite3.connect('petco.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO PETS (pet_id, name, breed)
                VALUES (?, ?, ?)
            ''', (pet_id, pet_name, breed))
            conn.commit()
            messagebox.showinfo("Success", "Pet added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Pet ID already exists.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def add_product(self):
        product_id = self.entry_product_id.get().strip()
        price = self.entry_product_price.get().strip()
        expiration_date = self.entry_expiration_date.get().strip()

        if not self.validate_input(product_id, price, expiration_date):
            messagebox.showerror("Input Error", "Please fill in all fields correctly.")
            return

        try:
            conn = sqlite3.connect('petco.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO PRODUCTS (idNumber, price, expirationDate)
                VALUES (?, ?, ?)
            ''', (int(product_id), int(price), expiration_date))
            conn.commit()
            messagebox.showinfo("Success", "Product added successfully!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Database Error", "Product ID already exists.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

    def validate_input(self, *args):
        return all(arg and (arg.isdigit() if i in [0, 4] else True) for i, arg in enumerate(args))

    def clear_inputs(self):
        # Clear all input fields and search results
        for widget in self.input_frame.winfo_children():
            widget.destroy()
        self.update_input_fields()  # Reset fields based on the selected type
        self.entry_search_id.delete(0, tk.END)  # Clear search input
        self.txt_output.delete(1.0, tk.END)  # Clear output

    def search_entry(self):
        search_id = self.entry_search_id.get().strip()
        entry_type = self.selected_type.get()

        # Clear previous search results before new search
        self.txt_output.delete(1.0, tk.END)

        try:
            conn = sqlite3.connect('petco.db')
            cursor = conn.cursor()
            if entry_type == "Employee":
                cursor.execute('SELECT * FROM EMPLOYEE WHERE employee_ID = ?', (search_id,))
            elif entry_type == "Customer":
                cursor.execute('SELECT * FROM CUSTOMERS WHERE customer_ID = ?', (search_id,))
            elif entry_type == "Department":
                cursor.execute('SELECT * FROM DEPARTMENT WHERE dept_ID = ?', (search_id,))
            elif entry_type == "Pet":
                cursor.execute('SELECT * FROM PETS WHERE pet_id = ?', (search_id,))
            elif entry_type == "Product":
                cursor.execute('SELECT * FROM PRODUCTS WHERE idNumber = ?', (search_id,))

            row = cursor.fetchone()
            if row:
                self.txt_output.insert(tk.END, str(row))
            else:
                messagebox.showinfo("Not Found", f"No entry found for {entry_type} ID: {search_id}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        finally:
            conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = PetcoApp(root)
    root.mainloop()
