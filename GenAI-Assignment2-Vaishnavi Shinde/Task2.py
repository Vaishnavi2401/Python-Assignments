order = [1200, 2500, 800, 1750, 3000]

final_values=[]

for order_amount in order:
    discount = 0
    
    if(order_amount>=2000):
        discount = 15
    elif(order_amount >= 1500 and order_amount < 2000):
        discount = 10
    elif(order_amount >= 1000 and order_amount < 1500):
        discount = 7
    else:
        discount = 0
    
    subtotal_amount = order_amount - ((discount*order_amount)/100)
    tax = (5*subtotal_amount)/100
    final_total= subtotal_amount + tax

    value = (order_amount, discount, final_total)
    final_values.append(value)

# print(final_values)
print("order_amount -> discount% -> final_amount")
for order_value in final_values:
    print(f"{order_value[0]} -> {order_value[1]}% -> {order_value[2]}")

total_revenue = 0
order_count_with_discount = 0
for order_value in final_values:
    total_revenue+=order_value[2]
    if(order_value[1]>0):
        order_count_with_discount+=1

print("Total revenue : ", total_revenue)
print("Order that receive the discount : ",order_count_with_discount)