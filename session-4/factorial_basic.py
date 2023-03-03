"""
    Factorial Without Functions
    Author:
"""
n=int(input('Enter n: '))
r=int(input('Enter r: '))

while(n>r):
    #calculating n factorial
    fact_n = 1
    for i in range(1,n+1):
        fact_n = fact_n*i
    #calculating r factorial
    fact_r = 1
    for i in range(1,r+1):
        fact_r = fact_r*i
    #calculating (n-r)! 
    fact_n_r = 1
    for i in range(1,n-r+1):
        fact_n_r = fact_n_r*i
    fact = fact_n/(fact_r)*(fact_n_r)
    print(fact)
    break