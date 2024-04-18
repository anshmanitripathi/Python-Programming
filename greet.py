import time
a = time.strftime('"%H":"%M":"%S"')
print(a)
if(int(time.strftime("%H")) >= 5 and int(time.strftime("%H")) <= 10 ):
    print("Good Morning Sir !")
elif (int(time.strftime("%H")) >= 10 and int(time.strftime("%H")) < 12 ):
    print("Good Noon Sir !")
elif (int(time.strftime("%H")) >= 12 and int(time.strftime("%H")) < 16 ):
    print("Good Afternoon Sir !")
elif (int(time.strftime("%H")) >= 16 and int(time.strftime("%H")) < 19 ):
    print("Good Evening Sir !")
elif (int(time.strftime("%H")) >= 19 and int(time.strftime("%H")) < 5 ):
    print("Good Night Sir !")

