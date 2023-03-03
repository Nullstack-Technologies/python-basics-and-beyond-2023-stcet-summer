print(
    [
     _ for _ in range(1, 51) 
     if (_ % 2 != 0 and _ % 3 != 0)
    ]
    )

for num in range(1, 51):
    if num % 2 != 0 and num % 3 != 0:
        print(num)
