def linear_search(list,key):
    for i in range(0,len(list)):
        if(list[i] == key):
            return i

list = [12,23,45,67,89]
a = linear_search(list,int(input("Enter element to be search : ")))
if(a!=-1):
    print("element found")
else:
    print("element found")
