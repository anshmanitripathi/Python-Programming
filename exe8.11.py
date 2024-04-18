def ispal(a):
    rev = a[::-1]
    l = len(a)
    c = (l+1)//2
    for i in range(0,c):
        if(rev[i]==a[i]):
            return True
        else:
            return False

a = [1,2,3,4,3,2,1]
d = ispal(a)
print(d)