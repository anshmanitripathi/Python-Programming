def isrev(w1,w2):
    if(w1==w2[::-1]):
        print("Yes")
    else:
        print("No")

a = input("input a word :")
b = input("input another word :")
isrev(a,b)