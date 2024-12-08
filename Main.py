import os

menu = [
    {"name": "Mozzarella Sticks", "price": 6.99},
    {"name": "Buffalo Wings", "price": 8.99},
    {"name": "Nachos with Cheese", "price": 7.99},
    {"name": "Classic Cheeseburger with Fries", "price": 12.99},
    {"name": "Grilled Chicken Salad", "price": 13.49},
    {"name": "Margherita (Medium)", "price": 10.99},
    {"name": "Pepperoni (Large)", "price": 14.99},
    {"name": "Cheesecake", "price": 5.99},
    {"name": "Chocolate Lava Cake", "price": 6.99},
    {"name": "Soft Drinks", "price": 2.50},
    {"name": "Coffee", "price": 3.00}
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("\nRestaurant Menu:")
    for i, item in enumerate(menu):
        print(f"{i}: {item['name']} - ${item['price']:.2f}")
        print("-" * 30)

prc = 0.0
order_list = []

clear_console()
show_menu()

while True:
    try:
        ord = int(input("\nEnter the item number you want to order (Enter 11 to finish): "))
        
        if ord == 11:
            break
        
        if 0 <= ord < len(menu):
            prc += menu[ord]["price"]
            order_list.append(menu[ord]["name"])
        else:
            print("Invalid item number. Please try again.")

        
        clear_console()
        show_menu()

    except ValueError:
        print("Invalid input. Please enter a number.")

clear_console()
print("\nYour Ordered Items:")
for item in order_list:
    print(f"{item}")

print(f"\nTotal price to pay: ${prc:.2f}")
