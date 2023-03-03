"""
    Convert Marks to Grades
"""


# initialise an empty variable
marks = '0'

# Keep Looping Until You get a non Number
while(marks.isnumeric()):
    marks = input("Enter a Valid Marks to Get a grade Else Quit:")

    # check whether the number is numeric
    if not marks.isnumeric():
        break
    
    # Cast to Integer
    marks = int(marks)

    # calculate grades
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
        break
    
    marks = str(marks)