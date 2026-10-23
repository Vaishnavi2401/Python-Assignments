
price = [100, 250, 400, 1200, 50]

price_with_gst = list(map(lambda x: x+(x*0.18), price))

print("Original price: ",price)
print("Price after GST:",price_with_gst)