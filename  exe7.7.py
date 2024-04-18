def count(letter,word):
    l=0
    w=0
    for ch in letter:
        l=l+1
    print(f"{l} times letters")
    for ch in word :
        if(ch==" "):
            w=w+1
    print(f"{w+1} times words")



a = input("input a word :")
b = input("input a sentence :")
count(a,b)
