def remove_item(inventory):
        [item_names,item_quantities,item_price]=inventory
        index = int(input("Enter the index of the item to remove: ")) - 1
        if 0 <= index < len(item_names):
            removed_item = item_names.pop(index)
            removed_quantity = item_quantities.pop(index)
            removed_price = item_price.pop(index)
            print(f"{removed_item} (Quantity: {removed_quantity}) (price: {removed_price}) removed from the inventory.")
        else:
            print("Invalid index. Please try again.")
