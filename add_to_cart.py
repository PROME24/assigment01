def add_to_cart(inventory):
        [item_names,item_quantities,item_price]=inventory
        cart=[]
        index = int(input("Enter the index of the item to add to the cart: ")) - 1
        if 0 <= index < len(item_names):
            quantity = int(input("Enter the quantity to add to the cart: "))
            price = int(input("Enter the price to add to the cart: "))
            if quantity > 0 and quantity <= item_quantities[index]:
                cart.append((item_names[index], quantity))
                cart.append((item_names[index], price))
                print(f"{quantity} quantity & {price} price {item_names[index]} added to the cart.")
            else:
                print("Invalid quantity. Please try again.")
        else:
            print("Invalid index. Please try again.")


