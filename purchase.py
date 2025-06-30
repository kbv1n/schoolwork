#cost per item: <10 is full price, 10-20 (inclusive) is 5% discount, and 21+ is 10% discount
#solution accepts a string input representing an item (dictionary key)
#solution accepts an integer input representing the number of items to be purchased
#solution outputs the item and total cost of purchase

purchase = {"bananas": 1.85, "steak": 19.99, "cookies": 4.52, "celery": 2.81, "milk": 4.34}

item = str(input())
quantity = int(input())
price = 0
discount = 0
if item in purchase and quantity < 10:
    price = purchase[item] * quantity
elif item in purchase and 10 < quantity < 20:
    price = (purchase[item] * quantity) * .95
    discount = 5
elif item in purchase and quantity > 20:
    price = (purchase[item] * quantity) * .90
    discount = 10
    
print(f'{item} ${price:.2f}')