try:
    cp = eval(input("Enter the cost of product : "))
    cgst = eval(input("Enter the rate of CGST : "))
    sgst = eval(input("Enter the rate of SGST : "))
except Exception as e:
    print(e)
    print("Invalid input")

CGST = (cgst/100) * cp
SGST = (sgst/100) * cp

total = cp + CGST + SGST

print("total payable abount is : ", total)

