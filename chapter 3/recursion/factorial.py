def factorial(n):
    if n == 1:                        #<- base case
        return 1
    else:
        return n * factorial(n - 1)   #<- Recursive case


print(factorial(5))