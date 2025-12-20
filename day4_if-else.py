#Conditional Statements(if- else)
#Conditional operators
# >, <, >=, <==, ==, !=

#if
num= int(input("Enter a number: "))

if (num <0):
    print("Number is zero")
else:
    print("Number is special")

marks= int(input("Enter marks: "))

#elif
if marks >=60:
    print("First devision")
elif marks >=40:
    print("Pass")
else:
    print("Fail")

# Nested if
num=  10
if (num< 0):
    print("Number is negative")
elif (num >0):
    if (num <= 10):
        print("Number is between 1--10")
    elif (num >10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")