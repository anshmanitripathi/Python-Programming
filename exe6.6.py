def fact(a):
    f=1
    for i in range(1,a+1):
        f=f*i
    print(f)

n = int(input("Enter the number : "))
fact(n)