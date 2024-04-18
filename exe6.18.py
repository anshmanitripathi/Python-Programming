def roots(a,b,c):
    if((pow(b,2)-(4*a*c)) < 0):
        print("Compex roots")
    if((pow(b,2)-(4*a*c)) > 0):
        print("Real roots")
    if((pow(b,2)-(4*a*c)) == 0):
        print("Equal roots")

roots((int(input("Enter a : "))),(int(input("Enter b : "))), (int(input("Enter c : "))))