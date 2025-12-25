name= input("Enter a student name: ")
m1= int(input("Enter marks 1:"))
m2=int(input("Enter marks 2:"))
m3=int(input("Enter marks 3:"))

total= m1 +m2 + m3
average= total/3

print("Name: ", name)
print("Total :", total)
print("Average :", average)

if average >= 60:
    print("Grade: A")
elif average >= 40:
    print("Grade: B")
else:
    print("Grade: C")

      

