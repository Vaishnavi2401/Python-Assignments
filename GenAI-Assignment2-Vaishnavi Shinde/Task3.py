condition = True
input_list = []

while(condition):

    print("Menu:")
    print("1.Add order amount to list")
    print("2.Print existing list")
    print("3.Quit-->type(q/Q) to quit")

    input_given=(input("Enter the selection from menu: "))

    if(input_given == '1'):

        try:
            input_order = input("Enter order amount: ")
            input_order_amount = int(input_order)

        except Exception as e:
            print("Error", e)
            continue
        else:    
            input_list.append(input_order_amount)
            print(input_list)
            final_values=[]
            for order_amount in input_list:
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
    elif (input_given == '2'):
        print("order_amount -> discount% -> final_amount")
        for order_value in final_values:
            print(f"{order_value[0]} -> {order_value[1]}% -> {order_value[2]}")

    elif (input_given == 'q' or input_given == 'Q'):
        break

    else:
        continue