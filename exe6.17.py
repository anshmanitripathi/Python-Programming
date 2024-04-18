def distance(a,b,c,d):
    x = c-a
    x = pow(x,2)
    y = d-b
    y = pow(y,2)
    w = pow((x+y),0.5)    #l = pow((((b-a)**2) + ((d-c)**2)),0.5)
    print(format(w,".2f"))
distance(4,4,2,2)