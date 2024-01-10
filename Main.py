from Command import Command
from View_Inventory import View_Inventory
from add_item import add_item
from remove_item import remove_item
from update_item import update_item
from add_to_cart import add_to_cart
from view_cart import view_cart

item_names = ['Laptop', 'Headphones', 'Keyboard', 'Mouse']
item_quantities = [10, 20, 15, 30]
item_price = [10,20,15,30]

isExit = False
while not isExit:
    x= Command()
    print(x)
    get_choice = int(input(" enter your command: "))
    if(get_choice == 1):
        get_inventory = View_Inventory([
            item_names,item_quantities,item_price
        ])
        print(get_inventory)
    elif(get_choice == 2):
        y = add_item([
            item_names,item_quantities,item_price
        ])
        print(y)
    elif(get_choice == 3):
        z=remove_item([item_names,item_quantities,item_price])
        print(z)
    elif(get_choice == 4):
        a=update_item([item_names,item_quantities,item_price])
        print(a)
    elif(get_choice == 5):
        b= add_to_cart([item_names,item_quantities,item_price])
    elif(get_choice == 6):
        b=view_cart([cart])
        print(b)
    elif(get_choice == 7):
        pass
    elif(get_choice == 8):
        isExit = True