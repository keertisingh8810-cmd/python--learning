#Sets they are unordered collection of data items and unchangeable and do not contain duplicate items

s={2, 4, 2, 6}
print(s)

info = {"Carla", 19, False, 5.9, 19}
print(info)

numbers = {1,2,3,4,5}
print(numbers)
numbers.add(6)
print(numbers)

for value in info:
    print(value)


# File Handling

#reading a file
f= open('data.txt', 'r')
text= f.read()
print(text)
f.close()

#writing a file, append
f= open('data.txt' , 'a')
f.write('Hello World!')
f.close()

with open('data.txt', 'a') as f:
    f.write("Hey I am inside with")



file = open("data.txt", "w")
file.write("Hello, this is my first file")
file.close()

file = open("data.txt", "r")
content= file. read()
print(content)
file.close()



