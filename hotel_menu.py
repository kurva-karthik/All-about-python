# define the menu of restaurent
menu = {
    'pizza':40,
    'pasta':50,
    'burger':60,
    'salad':70,
    'coffee':80,
}

# greet
print("welcome to PYTHON restaurent")
print("pizza: Rs 40\npasta: Rs50\nBurger: Rs60\nsalad: Rs70\ncoffee: Rs80")

order_total = 0
# 80 + 70 = 150
item_1 = input("enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1] 
    print(f"your item {item_1} has been added to your order")
    
else:
    print(f"ordered item {item_1} is not available yet!")
    
another_order = input("do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been to order")
    else:
        print(f"Ordered item {item_2} is not available!")
        
print(f"the total amount of items to pay is {order_total}")
