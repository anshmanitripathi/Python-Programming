def eva_Quadratic(a,b,c):
        D = (b**2) - (4*a*c)
        if(D==0):
            r1 = -b/(2*a)
            r2 = -b/(2*a)
            return r1 ,r2
        elif(D > 0):
            r1 = (-b/(2*a)) + pow(D,0.5)
            r2 = (-b/(2*a)) - pow(D,0.5)
            return r1, r2
        elif (D < 0):
            r1 = (-b / (2 * a)) + pow(D, 0.5)
            r2 = (-b / (2 * a)) - pow(D, 0.5)
            return r1, r2

a = int(input("Enter a : "))
b = int(input("Enter a : "))
c = int(input("Enter a : "))

r1 ,r2 = eva_Quadratic(a,b,c)

print(f"roots are r1 = {r1} and r2 = {r2}")