#Exception Handling

a= input("Enter the number:")
print(f"Multiplication table of {a}is: ")
try:
    for  i in range(1,11):
        print(f"{int(a)} * {i} = {int(a)*i}")
except:
    print("Invalid input")


print("Some imp lines of code")
print("End of program")



try:
    num = int(input("Enter an integer : "))
    a= [6,3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer")

except IndexError:
    print("Index Error")


try:
    a= int(input("Enter a number: "))
    b= int(input("Enter another number: "))
    print("Result:", a/b)
except ZeroDivisionError:
    print("Cannotdivide by zero")
except ValueError:
    print("Invalid input")
finally:
    print("Program ended")
    




