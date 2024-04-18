import math
class circle():
    def area(self,radius):
        a = math.pi * radius * radius
        print(f"area = {a}")

c1 = circle()
c1.area(6)