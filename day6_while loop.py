#while loop

i = 0
while(i<3):
    print(i)
    i= i+1

i = 0
while(i<=3):
    print(i)
    i= i+1

print("Done with the loop")

count= 5
while (count > 0):
    print(count)
    count= count - 1
else:
    print("I am inside else")

#Sum of digits
num= int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    sum_digits += num % 10
    num = num // 10

print("Sum of digits: ", sum_digits)

#Reverse a number
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    reverse = reverse * 10 + num % 10
    num = num // 10

print("Reversed number: ", reverse)

