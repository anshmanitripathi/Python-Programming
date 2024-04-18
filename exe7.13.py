def removevowels(word):
    v = ''
    for ch in word :
        if(ch!='a' and ch!='e' and ch!='i' and ch!='o' and ch=='u'):
            v=v+ch
    return(x)

a = input("input a word :")
x = removevowels(a)
print(x)