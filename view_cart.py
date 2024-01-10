from add_to_cart import add_to_cart

def view_cart():
        cart = add_to_cart([cart])
        print("\nShopping Cart:")
        for item, quantity in cart:
            print(f"{item}: {quantity} quantiity ")