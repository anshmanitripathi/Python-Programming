def deodd(a,b):
    new = []
    for i in range(a,b+1):
        if(i%2!=0):
            new.append(i)
    new.sort()
    new.reverse()
    print(new)

a = int(input("Enter start : "))
b = int(input("Enter end : "))
deodd(a,b)