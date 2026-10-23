
prices_list = []
def add_price(prices_list, price):
    prices_list.append(price)
    return prices_list

def get_average_price(price_list):
    sum = 0
    for p in price_list:
        sum+=p
    avg = sum/(len(price_list))
    return avg

def max_price(price_list):
    max = 0
    for p in price_list:
        if(p>max):
            max = p
    return max

while(True):
    print("Menu: ")
    print("1. Add price")
    print("2. Show Average price")
    print("3. Show higjhest price")
    print("4. Quit--(type(Q/q))")

    selected_option = input("Select the opttion from menu: ")

    if(selected_option == 'q' or selected_option == 'Q'):
        break

    if(selected_option == '1'):
        price = int(input("Enter the price: "))
        new_price_list = add_price(prices_list, price)
        print("Price list: ", new_price_list)

    if(selected_option == '2'):
        avg = get_average_price(prices_list)
        print("Average price is:", avg)

    if(selected_option == '3'):
        max = max_price(prices_list)
        print("Highest price is: ", max)