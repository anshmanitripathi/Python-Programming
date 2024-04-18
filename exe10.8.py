

class Prac:
 x=5 # attribute x
 def disp(self, x):
   x=30
   print(" The value of local variable x is ",x)
   print(" The value of instance variable x is ",x)
ob=Prac()
ob.disp(50)