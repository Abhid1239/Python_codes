import math as m
while(True):

    (x,y)=[int(l) for l in input("type the first coordinate \n").split(",") ]
    print(x,y)
    (a,b)=[int(l) for l in input("2nd coordinate\n").split(",")]
    print(a,b)
    (u,v)=[int(l) for l in input("3rd coordinate\n").split(",")]
    print(u,v)

    c=y-b
    d=x-a
    le=m.sqrt(c*c+d*d)
    fe=m.sqrt((b-v)**2 + (a-u)**2)
    ee=m.sqrt((v-y)**2 + (u-x)**2)
    lar=[fe,le,ee]
    lar.sort()

    if x==a==u or y==b==v:
        print("the line is a colinear line")
    else:
        print(le,fe,ee)
        if le==fe==ee:
            print("equilqteral")
        elif le==fe or fe==ee or ee==le:
            print("isoless")
        
        else :
            print("scalable")
            if le>fe and fe>=ee:
                cmp=m.sqrt(fe**2 + ee**2)
                if m.floor(le)==m.floor(cmp):
                    print("right angle fe")
            elif fe>le:
                cmp=m.sqrt(le**2 + ee**2)
                if m.floor(fe)==m.floor(cmp):
                    print("right angle le")
            else:
                cmp=m.sqrt(le**2 + fe**2)
                if m.floor(ee)==m.floor(cmp):
                    print("right angle ee")
    
                
        
            
    
    
