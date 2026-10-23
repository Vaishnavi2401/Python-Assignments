
gst = lambda price: (0.18*price)

#print(gst(100))

discount_amount = lambda price, discount: ((price * discount)/100) 

final_price = lambda price, discount=5: price - discount_amount(price, discount) + gst(price)


print(final_price(50,0))

print(final_price(1500,10))

print(final_price(500))