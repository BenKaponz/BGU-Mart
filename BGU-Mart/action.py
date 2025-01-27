from persistence import *

import sys
def process_action(product_id: int, quantity: int, activator_id: int, date: str):
    product = repo.products.find(id=product_id)
    if not product:
        return  

    product = product[0] 

    if quantity < 0:
        if product.quantity + quantity < 0:
            return  

    new_quantity = product.quantity + quantity
    repo.execute_command(f"""
        UPDATE products
        SET quantity = {new_quantity}
        WHERE id = {product.id}
    """)

    repo.activities.insert(Activitie(product_id, quantity, activator_id, date))
    
    
def main(args : list[str]):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            
            product_id = int(splittedline[0])
            quantity = int(splittedline[1])
            activator_id = int(splittedline[2])
            date = splittedline[3]
            
            process_action(product_id, quantity, activator_id, date)

if __name__ == '__main__':
    main(sys.argv)