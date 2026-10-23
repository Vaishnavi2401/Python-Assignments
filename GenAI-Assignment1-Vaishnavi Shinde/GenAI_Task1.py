#1...
product_names = ['Apple', 'Banana', 'Carrot', 'Dragon Fruit', 'Fig', 'Grapes']

#2...
sample_products = ('Apple', 50, 'Fruit')

#3...
print(f"Second Product: {product_names[1]} \nLast Product: {product_names[len(product_names)-1]}")

#4...
product_names.append('Himalayan salt')
product_names.append('Ink bottle')
print("\nProduct list:")
for product in product_names:
    print(product)

#Optional...
sample_products_list = list(sample_products)
print(sample_products_list)
sample_products_list[1] = 100
sample_products_tuple = tuple(sample_products_list)
print(sample_products_tuple)
