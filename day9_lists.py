marks =[3,5,6,"Harry", True]#len=5,index will start from 0 onwards
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

print(marks[-3]) #Negative index
print(marks[len(marks)-3]) #Positive index

if 7 in marks:
    print("Yes")
else:
    print("No")

print(marks[1:])
print(marks[1:-1]) #print(marks[1: 4])

num=[2,3,4,5,6,7,8,9,2]
print(num[:4])
print(num[1:8])
print(num[1:4:2])

#list comprehension
lst= [ i*i for i in range(10)]
print(lst)
lst = [ i*i for i in range(10) if i%2==0]
print(lst)


marks= [70,80,65,90]
print(marks)
print("First marks:", marks[0])
print("Total subjects:", len(marks))

marks.append(85)
print("After append:", marks)

marks.remove(65)
print("After remove:", marks)

total = sum(marks)
average = total / len(marks)
print("Average marks:", average)