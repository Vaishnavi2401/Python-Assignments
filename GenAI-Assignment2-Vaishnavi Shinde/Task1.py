try:
    order_amount = int(input("Enter the order amount: "))
except Exception as e:
    print("Error", e)
else:
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
    print("Subtotal amount: ", subtotal_amount)

    tax = (5*subtotal_amount)/100

    print("Tax: ", tax)

    final_total= subtotal_amount + tax

    print("Final amount: ", final_total)