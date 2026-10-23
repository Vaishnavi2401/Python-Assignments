daily=[200,150,0,400,50,-1,300]
total_sale = 0

for sale in daily:
    if(sale == -1):
        break
    elif(sale == 0):
        continue
    elif(sale > 0):
        total_sale+=sale
        print("Running total:", total_sale)

print("Total", total_sale)