a = int(input())
b = int(input())
c = int(input())

if(a>b):
    if(a>c):
        print("the largest number is a",a)
    elif(c>a):
        print("the largest number is c",c)
elif(b>a):
    if(b>c):
        print("the largest numebr is b",b)
    elif(c>b):
        print("the largest number is c", c)

