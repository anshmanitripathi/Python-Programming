def factor(num):
    print("Fctors are - ")
    for i in range(1,num+1):
        if(num%i==0):
            print(i)

factor(int(input("Enter the number : ")))