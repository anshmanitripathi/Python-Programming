eng = int(input("Enter the mark of english : "))
maths = int(input("Enter the mark of maths : "))
hin = int(input("Enter the mark of hindi : "))
chem = int(input("Enter the mark of chemistry : "))
phy = int(input("Enter the mark of physics : "))

sum = eng + maths + hin + chem + phy
per = (sum/5)
print("Total marks = ", sum)
print("percentage = ", per)