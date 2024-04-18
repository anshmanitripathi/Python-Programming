a = int(input('enter first number :'))
b = int(input('enter second number :'))
c = int(input('enter third number :'))
d = int(input('enter fourth number :'))

sum = a + b + c + d

for i in range(sum):
    if a==1 or b==i or c==i or d==i :
        large = i

print(" largest numer is ", large)