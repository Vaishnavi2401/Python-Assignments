
def apply_discount(price, discount_percentage = 5):
    if(discount_percentage > 60):
        discount_percentage = 60

    discount_amount = (price * discount_percentage)/100
    discount_price = price - discount_amount

    return discount_price


price1 = apply_discount(1000, 10)
price2 = apply_discount(500)

print(price1)
print(price2)