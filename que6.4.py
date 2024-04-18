def reverse(num):
    sum = 0
    while (num !=0 ):
        r = num%10
        sum = (sum*10) + (r)
        num = num//10
    print(f"Reversed number is {sum} ")

n = int(input("Enter the number : "))
reverse(n)
