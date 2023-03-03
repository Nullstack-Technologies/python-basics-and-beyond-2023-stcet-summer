# Program to convert marks to grades


marks = 55

# IF ELse ladder to print out the right grade
if marks >= 0 and marks < 40:
    print("F")
elif marks >= 40 and marks < 50:
    print("D")
elif marks >= 50 and marks < 60:
    print("C")
elif marks >= 60 and marks < 70:
    print("B")
elif marks >= 70 and marks < 80:
    print("A")
elif marks >= 80 and marks < 90:
    print("E")
elif marks >= 90 and marks <= 100:
    print("O")
else:
    print("Not Applicable")
