def GCD(a,b):
    d = min(a,b)
    while(d>0):
        if(a%d==0 and b%d==0 and d!=1):
            print(f"{d} is the greatest common divisor")
        d=d-1

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
GCD(a,b)