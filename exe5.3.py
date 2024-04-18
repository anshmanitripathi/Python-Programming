num = int(input("Enter the number : "))
d = 0
sum = 0
while(num!=0):
    d = num%10
    sum = sum + d
    num = num // 10
print(sum)