

def add_item(inventory):
    [item_names,item_quantities,item_price]=inventory
    
    name = input("enter the item name: ")
    quantity = int(input("enter the quantity available: "))
    price = int(input("enter item price: "))
    item_names.append(name)
    item_quantities.append(quantity)
    item_price.append(price)
    print(f"{name} added to the inventory successfully.")