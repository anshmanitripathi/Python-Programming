a = "Hello MY name is AnSh !!! hello ansh !!! "         "ansh !!!"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("ansh", "anup"))
print(a.split(" "))
print(a.capitalize())
print(a.center(20))
#print(len(a.center(20)))
print(a.count("ansh"))
print(a.endswith("!!!"))
print(a.endswith("name", 2 ,13))
print(a.find("is"))

b = "XCOWHDFIWKNOIWJFOJWFJFIWEIFIDNNOIWFWWIFNDSSFI"
c = "837984"
d = "cvshfhshuibsjbebvsvhbjevl"

print(a.isalnum())
print(b.isalnum())
print(c.isalnum())
print(d.isalnum())

print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(d.isalpha())

print(b.isupper())
print(d.islower())

e = "dfkfjosos \n ajdfio\n"
print(e.isprintable())

f = " "

print(a.isspace())
print(b.isspace())
print(f.isspace())

g = "Ansh Mani Tripathi"
print(g.istitle())

print(g.startswith("A"))

print(g.swapcase())

print(a.title())