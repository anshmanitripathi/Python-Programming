def count(word):
    v=0
    for ch in word :
        if(ch=="a" or ch=="i" or ch=="e" or ch=="o" or ch=="u"):
            v=v+1
    print(f"{v+1} vowels")



a = input("input a word :")
count(a)
