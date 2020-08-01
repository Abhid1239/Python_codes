class Points:
    def __init__(self ,x ,y ):
        self.x = x
        self.y = y

    def move(self, n = 1):
        self.x += n
        self.y += n
        
    def points(self):
        return self.x,self.y

    def __add__(m, n):                      #By Object Overloading
        return Points(m.x +n.x , m.y + n.y)
    
    def add(self,l):                        #BY CREATING methds
        return Points(self.x + l.x , self.y + l.y )
        

    def __str__(self):              #for string use of string as return is important
        return str(self.x)+","+str(self.y)


p1 = Points(4,5)
p2 = Points(2,3)
print(p1.points())
p1.move(4)

print(p1.points())
p3 =p1 + p2

p4 = p1.add(p2)

print(p4,p3,p1,p2)
