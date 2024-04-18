def isdubli(list):
    dub = []
    for i in list:
        if i not in dub:
            dub.append(i)
        else:
            return True
    return False

Lst = [4,6,2,1,6,7,4]
print(isdubli(Lst))
Lst1 = [1,2,3,12,4]
print(isdubli(Lst1))