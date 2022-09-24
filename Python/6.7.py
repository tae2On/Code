from dataclasses import dataclass


def factorial(n) : 
    data = 1
    for i in range(1, n + 1):
        data = data * i
    return data 

print(factorial(5))
print(factorial(7))
print(factorial(10))
