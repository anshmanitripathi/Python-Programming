def countB(word):
    c=0
    for ch in word:
        if(ch=="b" or ch=="B"):
            c=c+1
    print(f"B is {c} times")


a = input("Enter a word : ")
countB(a)

