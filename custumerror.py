a = int(input("Enter an number between 5 to 10 :"))
if(a<5 or a>10):
    raise ValueError("Value should be between 5 and 9")

print("program executed.")