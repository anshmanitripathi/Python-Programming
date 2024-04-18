#4. Write the function startEndVowels(word) which returns True if the word starts and ends
#with vowels.

def startendvowels(a):
    if(a.startswith("a" or "e" or "i" or "o" or "u") and a.endswith("a" or "e" or "i" or "o" or "u")):
        return True
    else:
        False

b = startendvowels("angfhi")
if(b==True ):
    print("true")
else:

    print("false")