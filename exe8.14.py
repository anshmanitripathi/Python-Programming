def Assign_grade(Lst):
    for Marks in Lst :
        if Marks >= 90:
            print("Student : ",Lst.index(Marks) + 1,'Marks =',Marks, "grade A")
        elif Marks >=80 and Marks<90:
            print("Student : ",Lst.index(Marks)+ 1,"Marks =",Marks," grade B")
        elif Marks >65 and Marks< 80 :
            print("Student : ",Lst.index(Marks)+ 1,"Marks =",Marks," grade C")
        elif Marks >=40 and Marks<=65:
            print("Student : ",Lst.index(Marks)+ 1,"Marks =",Marks," grade D")
        else:
            print("Student : ",Lst.index(Marks)+ 1,"Marks =",Marks," grade F")

a = []
for i in range(0,5):
    x = int(input(f"Enter the {i+1} student : "))
    a.append(x)

Assign_grade(a)