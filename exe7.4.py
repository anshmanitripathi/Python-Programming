w1 = "HELLO ANSH"
w2 = "HELLO ANSH"

print(w1)
print(w2)
print("The word that apper in w1 is also appear in w2")

for ch in w1:
    if ch in w2:
        print(ch,end="")
