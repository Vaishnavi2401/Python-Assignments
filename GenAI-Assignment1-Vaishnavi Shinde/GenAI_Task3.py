#1..
price_dict = {'Apple':100, 'Banana': 40, 'Carrot': 80, 'Dragon Fruit': 200, 'Fig': 70, 'Grapes': 120}

#2..
price_dict['Jackfruit'] = 400

print(price_dict)

price_dict['Apple'] = 150

print(price_dict)

if 'Fig' in price_dict:
    price_dict.pop('Fig')

print(price_dict)

#3..
sum = 0
for key, value in price_dict.items():
    sum +=value

avg = sum/len(price_dict)
print(f"Average of all prices is: {avg}")

#Optional...
max = 0
for key, value in price_dict.items():
    if(max < value):
        max = value

min = max
for key, value in price_dict.items():       
    if(min > value):
        min = value

print(f"Max price is: {max}\nMin price is: {min}")