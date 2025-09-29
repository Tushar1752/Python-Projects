#Cafe management system minor project

menu={
    'burger':40,
    'fries':15,
    'soda':10,
    'salad':20,
    'dessert':25,
}
print("welcome to the restaurant")
print(" burger=40 \n fries=15 \n soda=10 \n salad=20 \n dessert=25")
order_amount=0

item1=input('enter your first item:')
if item1 in menu:
      order_amount+=menu[item1]
      print(f'{item1} added to your order')
else:
       print(f'sorry {item1} is not available')
       print("Wrong input Please try again")
       exit()
another_item=input("Do you wish for more item (Yes/No):")
if another_item == 'Yes':
    item2=input("enter your second item:")
    if item2 in menu:
        order_amount+=menu[item2]
        print(f'{item2} added to your order')
    else:
      print(f'sorry {item2}is not available')
else:
     print("Thank you for your order")

print(f"The total amount you have to pay is {order_amount}")