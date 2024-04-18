def reverse(list):
    l = len(list)
    c=1
    rev = []
    for i in list:
        rev.append(list[l-c])
        c=c+1
    print(f"reverse = {rev}")

a = []
for i in range(0,5):
    x = int(input(f"Enter the {i} element : "))
    a.append(x)

reverse(a)
