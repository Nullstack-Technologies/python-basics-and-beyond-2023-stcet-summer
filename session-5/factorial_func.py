"""
    Factorial Without Functions
    Author:
"""

def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact

n=int(input('Enter n: '))
r=int(input('Enter r: '))


nCr = factorial(n) / factorial(r) * factorial(n-r)
print(nCr)
