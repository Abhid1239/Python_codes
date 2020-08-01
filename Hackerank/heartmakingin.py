import math

c='♥'
width = 40

print ((c*2).center(width//2)*2)

for i in range(1,width//10+1):
    print (((c*int(math.sin(math.radians(i*width//2))*width//4)).rjust(width//4)+
           (c*int(math.sin(math.radians(i*width//2))*width//4)).ljust(width//4))*2)

for i in range(width//4,0,-1):
    print ((c*i*4).center(width))
print ((c*2).center(width))


thickness = 4
#Bottom Cone
for i in range(thickness):
    print ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6) 

#Bottom Cone
for myShift in range(1,7):
    print ("")
    print ("|Btm Cone |".rjust(thickness*myShift))
    print ("")
    for i in range(thickness):
        print (
                ('O'*(thickness-i-1)).rjust(thickness,'"')+
                'v'+
                ('X'*(thickness-i-1)).ljust(thickness,'^')
            ).rjust(thickness*myShift,'.')


