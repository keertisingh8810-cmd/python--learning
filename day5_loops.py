#for loop
#print numbers from 1 to 10

for i in range(1, 11):
    print(i)

#print even numbers from 1 to 20

for i in range(2, 21, 2):
    print(i)

#print table of a number
num = int(input("Enter a number: "))

for i in range(1,11):
    print(num, "x", i, "=", num*i)

name= 'Abhinav'
for i in name:
    print(i)
    if(i=='b'):
        print("This is something special")

colors= ["Red", "Green", "Blue", "Yellow"]
for color in colors:
  print(color)
  for i in color:
      print(i)

for i in range(5):
    print(i)

for i in range(5):
    print(i+1)