class cat:
    def __init__(self, colour, legs):
        self.colour = colour
        self.legs = legs
        
felix = cat("black",4)
rover = cat("brown",5)
nilya = cat("white",6)
new={felix,rover,nilya}
for i in new:
    print(i.colour,i.legs)

