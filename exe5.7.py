num = int(input("Enter the number : "))
x = num
d = 0
c = 0
sum = 0
while(num>0):
    d = num%10
    c = c+1
    num = num //10

num = x
while(num>0):
    d = num%10
    sum = sum + (d**c)
    num = num //10

if(sum == x):
    print("Amstrong number")
else:
    print("Not a amstrong number")
