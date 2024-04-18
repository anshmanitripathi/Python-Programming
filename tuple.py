tup = (1,3,4,5)
print(type(tup))
tup1 = (1,)
print(type(tup1))

a = (3,2,3,42,524,53,245,245,56,76)
print(a[0])
print(a[8])
print(a[-1])

if 524 in a:
    print("Yes")
else:
    print("no")

print(a[2:8:2])


#operation on tuple
# tuples are immutable

b = [3,23,4,2,3,4,5,6,7,8,3,3,3,3,]
print(b.count(3))
print(b.index(3))
print(b.index(3,3,8))
print(len(b))

temp = list(b)
temp.append(99)
b = tuple(temp)
print(b)