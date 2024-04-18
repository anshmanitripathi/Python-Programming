s = {2,7,8,6,9}
print(s) #sets are immutable

s1 = {"hello",5,7,8,8,7,5,"ansh"}
print(s1)     #it doesnot repeat values

for value in s1:
    print(value)  #to print values in set

print(s1) #to print set1

#set manipulation :

s1 = {1,3,8,9,5,6}
s2 = {0,1,2,5,7,86,3}

#print(s1.union(s2))
#print(s1,s2)

#s1.update(s2)

#print(s1)

s3 = s1.intersection(s2)

print(s3)

s4 = s1.symmetric_difference(s2)
print(s4)

s5 = s1.difference(s2)
print(s5)

s6 = s1.isdisjoint(s2)
print(s6)

s7 = s1.issuperset(s2)
print(s7)

s8 = s1.issubset(s2)
print(s8)

s1.add(49) #to add element
print(s1)

s1.remove(49) #to remove element (if item is not present it gives a error)
print(s1)

s1.discard(49) #to remove element (if item is not present it does not gives a error)
print(s1)

item = s1.pop() #to pop a element from a set
print(s1)
print(item)

# del s1                     delete the set
# clear s1                   remove all the element from the set

if 49 in s1:
    print("yes")
else:
    print("no")
