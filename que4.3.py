temp = input("Enter the temperature warm/cold : ")
hum = input("Enter the humidity dry/humid : ")

t = temp.lower()
h = hum.lower()

if(t=="warm"):
    if(h=="dry"):
        print("Play Basketball")
    else:
        print("Play tennis")
elif(t=="cold"):
    if(h=="dry"):
        print("Play cricket")
    else:
        print("Swim")