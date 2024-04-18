sum = 0
def sod(num):
    if(num==0):
        return 0
    r = num % 10
    sum = r + sod(num//10)
    return sum

print(sod(int(input("Enter number : "))))