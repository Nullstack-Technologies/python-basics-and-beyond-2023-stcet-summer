import random


class Animal:

    def __init__(self, age):
        self.age = age

    def speak(self):
        pass


class Dog(Animal):

    def speak(self):
        print("bark")


class Student(Animal):

    def __init__(self, name, age, department):
        super().__init__(age)
        self.name = name
        self.department = department

    def speak(self):
        print(random.choice(["I need Food",
                       "GB Sir",
                       "SOM Sir",
                       "Game",
                       "SLEEP"
                       ]))


a = Animal(10)
d = Dog(12)
student = Student("Amritesh", 90, "ECE")
# a.speak()
# d.speak()
# student.speak()
# print(a.age)
# print(d.age)

print(isinstance(a, Animal))
print(isinstance(d, Dog))
print(isinstance(d, Animal))
