#2. Write the function Echo_Word(word) which takes a word as the argument and returns a
#word that repeats itself based on the number of letters in the word.

def eco(w):
    c=0
    for ch in w:
        c=c+1
    print(c*w)

eco("hello")