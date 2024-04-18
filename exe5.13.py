sum =0
a = 0
for i in range(1,21):
    if(i%3==0 or i%2==0 or i%5==0):
        a = a +1
    else:
        print(i)
        sum = sum +i

print("sum =", sum)