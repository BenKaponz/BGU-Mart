from persistence import *

def print_activities():
    rows = sorted(repo.activities.find_all(), key=lambda activity: activity.date) 
    print("Activities")
    for activity in rows:
        print(activity)

def print_branches():
    rows = sorted(repo.branches.find_all(), key=lambda branch: branch.id)  
    print("Branches")
    for branch in rows:
        print(branch)

def print_employees():
    rows = sorted(repo.employees.find_all(), key=lambda employee: employee.id)  
    print("Employees")
    for employee in rows:
        print(employee)

def print_products():
    rows = sorted(repo.products.find_all(), key=lambda product: product.id)  
    print("Products")
    for product in rows:
        print(product)

def print_suppliers():
    rows = sorted(repo.suppliers.find_all(), key=lambda supplier: supplier.id)  
    print("Suppliers")
    for supplier in rows:
        print(supplier)

def print_employees_report():
    employees = repo.employees.find_all()
    branches = {branch.id: branch.location for branch in repo.branches.find_all()}
    activities = repo.activities.find_all()
    products = {product.id: product.price for product in repo.products.find_all()}

    employees = sorted(employees, key=lambda emp: emp.name) 

    print("Employees report")
    for employee in employees:
        total_sales = sum(
            abs(activity.quantity) * products.get(activity.product_id, 0)
            for activity in activities
            if activity.activator_id == employee.id and activity.quantity < 0
        )

        branch_location = branches.get(employee.branche, "Unknown")
        print(f"{employee.name} {employee.salary} {branch_location} {total_sales}")

def print_activities_report():
    products = {product.id: product.description for product in repo.products.find_all()}
    employees = {employee.id: employee.name for employee in repo.employees.find_all()}
    suppliers = {supplier.id: supplier.name for supplier in repo.suppliers.find_all()}

    activities = sorted(repo.activities.find_all(), key=lambda activity: activity.date)  

    print("Activities report")
    for activity in activities:
        description = products.get(activity.product_id, "Unknown")
        quantity = activity.quantity
        seller = None
        supplier = None

        if activity.quantity < 0:  
            seller = employees.get(activity.activator_id, None)
        else:  
            supplier = suppliers.get(activity.activator_id, None)

        print(f"('{activity.date}', '{description}', {quantity}, {repr(seller)}, {repr(supplier)})")
        
        
def main():
    print_activities()
    print_branches()
    print_employees()
    print_products()
    print_suppliers()
    print_employees_report()
    print_activities_report()

if __name__ == '__main__':
    main()