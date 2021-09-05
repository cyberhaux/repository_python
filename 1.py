def factorial(n: int):
    f = 1
    if n < 0:
       print("Sorry, factorial does not exist for negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, n + 1):
            f *= i
        return f

    
factorial(4)
