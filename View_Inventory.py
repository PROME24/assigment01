def View_Inventory(inventory):
    [item_names,item_quantities,item_price]= inventory
    print_inventory = ""
    for i in range(len(item_names)):
        item = item_names[i]
        quantity = item_quantities[i]
        price = item_price[i]
        print_inventory += f"{i+1}. Item Name :{item}; Item Quantity: {quantity};Item price: {price}\n"

    return print_inventory