
menu = {
    "pakistan" : {
        'daal chawal' : 150,
        'palak gosht' : 250,
        'malai boti' : 1000
    },
    "chinese" : {
      'Buddha  Soup'  : 6900,
       'sea cucumber' : 750,
       'chinese rice' : 500
    },
    "spanish" : {
        'Tortilla de Patatas' : 2000,
        'Gazpacho' : 1750,
        'Jamón Ibérico' : 988
    }
}

order_list = []

print(" Welcome to Restaurant ")

while True:
    print("\nPlease Select a category:")
    for i, category in enumerate(menu.keys(),1):
        print(f"{i}. {category}")
    print("4. wrap up the order")

    choice = int(input("Enter your choice  - "))
    

    if choice == 4:
        break

    category = list(menu.keys())[choice - 1]

    print(f"\n {category} Menu ")
    for i, (item, price) in enumerate(menu[category].items(), 1):
        print(f"{i}. {item} - Rs.{price}")
        print('---------')

    item_choice = int(input("Select any item: "))
    item = list(menu[category].keys())[item_choice - 1]
    order_list.append((item, menu[category][item]))
    for j in enumerate(order_list,1):
        print(f"{j}{item} have been added to your order!")
        break
    
    for item, price in order_list:
        print(f"{item} - Rs.{price}")

feedback = input("How was your experience? (Good/Mid/Bad): ")

total_bill = sum(price for _, price in order_list)
print("\n Your Bill Receipt ")
for item, price in order_list:
    print(f"{item} - Rs.{price}")
print(f"Total: Rs.{total_bill}")
paid = int(input("give money."))


while paid < total_bill:
    amount = int(input("Your amount is less, give more money: "))
    paid += amount

remain = paid - total_bill


print(f"Your remaining rupees are : {remain}")
print(f"Feedback: {feedback}")
print(" Thank you for visiting the Restaurant")




    
    
