num = int(input("Enter a four digit number"))
a = num%10
num = num//10
b = num%10
num = num//10
c = num%10
num = num//10
d = num%10

sum = a + b + c + d
print(sum)