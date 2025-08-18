# Task 1

def factorial(n):
    result = 1
    if n < 2:
        return 1
    else:
        for i in range(2,n+1):
            result = result * (i)
        return result
num = int(input("Enter a number: "))
print(factorial(num))
