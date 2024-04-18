def fact(a):
    if(a==0):
        return 1
    return a* fact (a-1)

a = fact(int(input("Enter the number : ")))
print(a)