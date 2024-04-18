def charremove(word,letter):
    c =word.replace(f"{letter}","",)
    print(c)

a = input("Enter thr word : ")
b = input("Enter term to remove : ")
charremove(a,b)