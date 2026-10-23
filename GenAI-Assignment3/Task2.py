
def factorial(n):
    fac = 1
    if(n == 0 or n == 1):
        return 1
    elif(n < 0):
        print("Error: Can't able to file factoial for negative number")
        return -1
    else:
        fac=n * factorial(n-1)
        return fac

factorial_result1 = factorial(5)
print("Factorial of 5 is: ", factorial_result1)

factorial_result2 = factorial(0)
print("Factorial of 0 is: ", factorial_result2)

factorial_result3 = factorial(-3)


