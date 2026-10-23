#product_names = ['Apple', 'Banana', 'Carrot', 'Dragon Fruit', 'Fig', 'Grapes']

#1..
categories = ['vegetable', 'fruits', 'groceries']

categories_set= set(categories)

print("Categories Set: ",categories_set)

#2..
categories_set.add('vegetable')

print("Categories Set after adding vegetable as category : ",categories_set)

category = 'vegetable'

#3...
check_status= category in categories_set

print(check_status)

# Optional...
print("Total no of unique categories in set", len(categories_set))