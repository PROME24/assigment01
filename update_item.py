
def update_item(inventory):
        [item_names,item_quantities,item_price]=inventory
        index = int(input("Enter the index of the item to update: ")) - 1
        if 0 <= index < len(item_names):
            new_quantity = int(input("Enter the new quantity: "))
            new_price = int(input("enter new price: "))
            item_quantities[index] = new_quantity
            item_price[index]= new_price 
            print(f"{item_names[index]} quantity updated to {new_quantity} & price update to  {new_price}.")
        else:
            print("Invalid index. Please try again.")