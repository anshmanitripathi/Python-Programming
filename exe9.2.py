#binary search.

def binary_search(list,key):
    low = 0
    high = len(list) - 1
    while(low<=high):
        mid = (low + high)//2
        if(list[mid]==key):
            return mid
        elif(list[mid]>key):
            high = mid - 1
        else:
            low = mid + 1
    return -1
lst = [10, 20, 30, 34, 56, 78, 89, 90]
c = binary_search(lst,int(input("Enter item : ")))
if(c!=-1):
    print("item found")
else:
    print("item not found")
