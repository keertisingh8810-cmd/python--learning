#tuples inko change nhi kar sakte
# tuples are immutable, Strings are immutable, Lists are mutable
tup = (1,) #if we'll write tup =(1) it's an error
tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup), tup)
print(len(tup), tup)
print(tup[0])
print(tup[-1])
print(tup[2])

tup2 = tup[1:4]
print(tup2)

subjects = ("Maths", "DBMS", "OS")
print(subjects)
print(subjects[0])


#Dictionaries
dic = {
    "Harry": "Human being",
    "Spoon":"object"
}

print(dic["Harry"])

dic = {
    344:"Neha",
    345:"Pooja",
    678:"Zakir"
}
print(dic[345])

info= {"name":"Karan", 'age':19, 'eligible': True}
print(info.get("name"))

print(info.keys())
print(info.values())


for key in info.keys():
    print("The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print("The value corresponding to the key {key} is {value}")

student= {
    "name": "Roma",
    "age": 22,
    "course": "MCA"
}
print(student)
print(student["name"])


student["marks"] = [70,80,90]

total= sum(student["marks"])
average= total/ len(student["marks"])

print("Average marks:", average)
