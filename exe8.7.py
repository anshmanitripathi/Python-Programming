def lstsplit(lst,n):
    lst1 = lst[:n]
    lst2 = lst[n:]
    print(lst1)
    print(lst2)

a = [10,20,30,40,3,4,5,35,234,56,32,4,5,8]
print("original list : ",a)
lstsplit(a,5)