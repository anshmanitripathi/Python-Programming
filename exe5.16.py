term = int(input("Enter the number of terms :"))
a=0
b=1
print(a)
print(b)
for i in range(1,term-2):
        c = a + b
        a=b
        b=c
        print(c)
