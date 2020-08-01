import math as m
def cst(x,y,a,b):
    d=m.sqrt((x-a)**2 + (y-b)**2)
    return d

'(x,y,a,b)=[int(l) for l in input("enter both cordinate").split(",")]'
(x,y,a,b)=[input("this"),input("what"),input("for"),input("what")]

print(cst(x,y,a,b))
