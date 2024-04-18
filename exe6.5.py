def max(a,b):

    if(a>b):
        print(f"{a} is greater")
    elif(b>a):
        print(f"{b} is greater")
    elif(a==b):
        print("NO.are equal")

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
max(a,b)