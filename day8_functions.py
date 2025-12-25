def calculateGmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)

def isGreater(a,b):
    if(a>b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")

def islesser(a,b):
    pass # just to pass and process

a= 9
b= 8
isGreater(a,b)

# gmean1 = (a*b)/ (a+b)
# print(gmean1)
calculateGmean(a,b)

c= 8
d= 7
isGreater(c,d) #short form of below 4 lines
# if(c>d):
#     print("First number is greater")
# else:
#     print("Second number is greater or equal")
# gmean2 = (c*d)/ (c+d)
# print(gmean2)
calculateGmean(c,d)




