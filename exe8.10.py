def eveninbtw(a,b):
    c = []
    for i in range(a,b):
        if(i%2==0):
            c.append(i)
    return c
print(eveninbtw(1,50))
