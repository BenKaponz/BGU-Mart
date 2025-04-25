# 🛒 BGU Mart
**Supermarket Management System – SPL 2025 @ BGU**

A Python-based inventory and activity management system for supermarket chains, developed as part of the **Systems Programming Lab (SPL)** course at Ben-Gurion University.  
The system uses an SQLite3 database to track branches, employees, products, suppliers, and sales/delivery activities.

---

## 🔧 Technologies Used
- **Python 3.9+** – Core implementation
- **SQLite3** – Embedded database engine
- **Command-line Interface** – Standalone scripts for initialization, actions, and reporting

---

## 💡 Project Structure
```
BGU-Mart/
├── bgumart.db            # SQLite database (created at runtime)
├── initiate.py           # Initializes the database from a configuration file
├── action.py             # Executes activity actions (sales/deliveries)
├── printdb.py            # Prints database tables and reports
├── config.txt            # Sample configuration file
├── actions.txt           # Sample activity input file
└── README.md             # Project documentation
```

---

## 🏬 Database Schema

| Table        | Description |
|--------------|-------------|
| `employees`  | ID, name, salary, and branch assignment |
| `suppliers`  | Supplier ID, name, contact information |
| `products`   | Product ID, description, price, quantity in stock |
| `branches`   | Branch ID, location, and employee count |
| `activities` | Logs of sales and deliveries (product ID, quantity, actor ID, date) |

---

## 📦 Configuration File Format (`config.txt`)

Each line defines one entity using the following format:

| Prefix | Entity     | Format |
|--------|------------|--------|
| `B`    | Branch     | `B,<id>,<location>,<num_employees>` |
| `E`    | Employee   | `E,<id>,<name>,<salary>,<branch_id>` |
| `P`    | Product    | `P,<id>,<description>,<price>,<quantity>` |
| `S`    | Supplier   | `S,<id>,<name>,<contact_info>` |

Example:
```
B,3,Chicago,40
E,106,Sue Davis,75000,3
P,5,Mango,2,7
S,6,Jkl Enterprises,(678) 901-2345
```

> ⚠ Do **not** insert the record-type prefixes (E, S, P, B) into the database.

---

## 📈 Actions File Format (`actions.txt`)

Format:
```
<product_id>,<quantity>,<activator_id>,<date>
```

- `quantity > 0` → delivery (by supplier)  
- `quantity < 0` → sale (by employee)

Example:
```
3,500,56,20230110      # Delivery from supplier 56
100,-500,1234,20230110 # Sale by employee 1234
```

> ⚠ Sale is performed only if product stock is sufficient — otherwise, it's ignored silently.

---

## 🚀 How to Run

### 1. Initialize the Database
```bash
python3 initiate.py config.txt
```

### 2. Perform Actions
```bash
python3 action.py actions.txt
```

### 3. Print Reports
```bash
python3 printdb.py
```

---

## 📊 Report Output Formats

### 👩‍💼 Employees Report
```
<name> <salary> <branch_location> <total_sales_income>
```

Sorted by name.

### 📆 Activity Report
```
<date> <product_description> <quantity> <seller_name> <supplier_name>
```

- For delivery: `seller_name = None`  
- For sale: `supplier_name = None`

Sorted by date.

---

## 🧪 Testing
Validate memory and SQL correctness with:
```bash
valgrind --leak-check=full --show-reachable=yes python3 action.py actions.txt
```

---

## 📚 Course Information
- **Course:** SPL – Systems Programming Lab  
- **Institution:** Ben-Gurion University of the Negev  
- **Year:** 2025  
- **Environment:** Linux CS Lab, SQLite3, Python 3.9+

---

## 🧑‍💻 Authors

**Ben Kapon**  
Student at BGU  
[LinkedIn](https://www.linkedin.com/in/ben-kapon1/)

**Itay Shaul**  
Student at BGU  
[LinkedIn](https://www.linkedin.com/in/itay-shaul/)

---
