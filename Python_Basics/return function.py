def max(x, y):
    if x >=y:
        return x
    else:       #this is the red text
        return y

set = max
print(set(4,7))

z= max(8,3)
print(z)


def dota(func, x, y):
    return func(func(x, y), func(x, y))
a=5
b=4

print(dota(max, a, b))

def square(x):
    return x*x

def test(func, x):
    print(func(x))
   
    
test(square, 42)

