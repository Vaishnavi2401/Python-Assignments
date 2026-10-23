
price=[100, 250, 400, 1200, 50, 2000, 850]

price_greater = list(filter(lambda p: p>500, price))

price_less = list(filter(lambda p: p<=500, price))

print("Price greater then 500:",price_greater)

print("Price less than or equal to 500:",price_less)