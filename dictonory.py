dic = {"Ansh": "Mani tripathi",
       "Anup" : "Mishra"}

print(dic)
print(dic["Ansh"])

dic1 = { 1 : "Ansh",
         2 : "Anup",       # 1 - key , "Ansh" - value
         3 : "Harsh"}

#print(dic1["aadi"])   it gives error because aadi doesnt exist in dic1
print(dic1.get("aadi"))     #it does not gives error even aadi doesnt exist in dic1  it return "none
print(dic1.keys()) #to get all the keys
print(dic1.values()) #to get all the values

