
a = ''' 1) FOR 10000 RUPEE
Question: Where is Fort William located ? \n 1) Chennai \n 2) Goa \n 3) Kolkata \n 4) Mysore'''
b = ''' 2) FOR 25000 RUPEE
Question: Name this Indian Tennis player who has turned Hollywood filmmaker?
1) Leander Paes
2) Mahesh Bhupathi
3) Vijay Amritraj
4) Ashok Amritraj'''
c = ''' 3) FOR 50000 RUPEE
Question: Sishu is the literary work of wh3ich Indian author?
1) Vikram Seth
2) Jawaharlal Nehru
3) Rabindranath Tagore
4) Arundhati Roy'''
d = ''' 4) FOR 100000 RUPEE
Question: Which of these Cities located in the state of Gujarat is famous for zari production?
1) Surat
2) Rajkot
3) Surendranagar
4) Ahmedabad'''

print(a)
A = int(input("Answer : "))
if(A==3):
    print("Congratulations! you won 10000 rupees.")
else:
    print("You lose!")

if(A==3):
  print(b)
  B = int(input("Answer : "))
  if(B==4):
    print("Congratulations! you won 25000 rupees.")
  else:
    print("You lose!")
else:
    exit(0)

if(B==4):
 print(c)
 C = int(input("Answer : "))
 if(C==3):
    print("Congratulations! you won 10000 rupees.")
 else:
    print("You lose!")
else:
    exit(0)

if(C==3):
 print(d)
 D = int(input("Answer : "))
 if(D==1):
    print("Congratulations! you won 10000 rupees.")
 else:
    print("You lose!")
else:
    exit(0)
