
def process_price(prices):

    discounted_prices = list(map(lambda p: p-(0.10*p), prices))

    filtered_prices = list(filter(lambda p: p>300, discounted_prices))

    return discounted_prices, filtered_prices

discounted_prices, filtered_prices = process_price([100, 500, 900, 50, 750])

print(f"Discounted prices: {discounted_prices}\nFiltered Prices: {filtered_prices}")