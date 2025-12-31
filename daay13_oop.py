#oop- classes and objects

class Person:
    name= "Harry"
    occupation= "Software Developer"
    networth= 10
    def info(self):
        print(f"{self.name} is a {self.occupation}") #self vo object jiske liye method call kiya ja rha hai

a= Person()
b= Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nikita"
b.occupation = "HR"

a.info()
b.info()

class Student:
    def _init_(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Marks:", self.marks)

s1 = Student("Rahul", 85)
s1.display()

s2 = Student("Amit", 90)
s2.display()


