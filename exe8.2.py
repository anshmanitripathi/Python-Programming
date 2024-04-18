a = [x**2 for x in range(1,11)]
print(a)
b = [x**3 for x in range(1,11)]
print(b)

c = [x for x in a if(x%2==0)]
print(c)