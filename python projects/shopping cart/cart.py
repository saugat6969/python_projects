foods=[]
prices=[]
total=0
while True:
    food=input('Enter what you want to buy(q to exit):')
    
    if food.lower()=='q':
        break
    else:
        price=float(input('Enter the price of item:$'))
        foods.append(food)
        prices.append(price)
print("___your cart___")    
for food in foods:
    print(food)
total+=price
print("__total price__:$",total)