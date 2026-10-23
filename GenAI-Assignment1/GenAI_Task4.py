
price_dict = {'Apple':100, 'Banana': 40, 'Carrot': 80, 'Dragon Fruit': 200, 'Fig': 70, 'Grapes': 120}

product_names = ['Apple', 'Banana', 'Carrot', 'Dragon Fruit', 'Fig', 'Grapes']

categories = ['vegetable', 'fruits', 'groceries']


#1..
list_of_tuples = list(price_dict.items())

product_list = [(name, price, categories[1]) for name, price in list_of_tuples]

product_list = [
    (name, price, 'vegetable' if name == 'Carrot' else category)
    for name, price, category in product_list
]

print("Product Catalog: ",product_list)

#2..
category_to_product={}

for category in categories:
    category_to_product[category]=[]
    for product in product_list:
        if(product[2] == category):
            category_to_product[category].append(product[0])

print("Product with price and category: ",category_to_product)

#3..
cat_with_max_size = ''
cat_size = 0
for key, value in category_to_product.items():
    if(len(value) > cat_size):
        cat_size=len(value)
        cat_with_max_size=key

print("Category products which have max no of size: ",category_to_product[cat_with_max_size])
    

