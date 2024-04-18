def dec_bin(num):
    c=0
    sum = 0
    while(num!=0):
        r = num%2
        sum = sum + r*pow(10,c)
        num = num//2
        c = c + 1
    print(f"Binary number is {sum}")

dec_bin(int(input("Enter decimal number : ")))