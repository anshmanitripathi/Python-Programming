def expo(base,exp):
    if(exp>=0):
       return (base**exp)
    else:
        print("Enter the positive exponent")
base = int(input("Enter base : "))
exp = int(input("Enter exponent : "))
print(expo(base,exp))