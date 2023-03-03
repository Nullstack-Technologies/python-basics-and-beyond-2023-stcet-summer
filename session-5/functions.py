# def greet():
#     print("hello")

# greet()

# def add(x, y):
#     print(f"Sum is {x + y}")

# add(3, 4)

# def add(x, y):
#     sum = x + y
#     return sum

# print(add(3, 4, 5))


# def add(*args):
#     sum = 0
#     for number in args:
#         sum += number
#     return sum

# print(add(1, 2, 3, 4, 5, 6, 7))


# def increment(num, by=1):
#     return num + by

# print(increment(3))


# def compound_interest(p, r, n):
#     ci = 0
#     ci = p*((1+(r/100))**n)
#     return ci

# print(compound_interest(1000, 10, 3))


# def person(**kwargs):
#     print(kwargs)

# person(
#     name="Nauman",
#     Age=200, 
#     designation="developer"
# )


# def compound_interest_two(**kwargs):
#     print(kwargs["p"])
#     print(kwargs.get("r"))
#     print(kwargs.get("n"))


# print(compound_interest_two(
#     p=200, r=10)
# )












# numbers = input("Enter Numbers to add:")
# numbers = numbers.split()
# for i, number in enumerate(numbers):
#     numbers[i] = int(number)
# print(numbers)
# add(*numbers)



x = 5

def hi():
    global x
    x = 6
    print(x)


hi()
print(x)


