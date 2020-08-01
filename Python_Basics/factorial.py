n=5
m=1
m1=1
while n >= 1 :
    n1 = n-1
    m= n*n1

    n-=1
    print(m)


x=4
n=x*(x-1)
print(n)


for n in range(5) :
    m= n*n+1
    m=m+n
print(m)


s= n*n-1*n-2*n-3*n-4*n-n+1

def fact(x):
    if x==1:
        return 1
    else :
        return x*fact(x-1)


print(fact(5))

x=3
if x==1:
    print(x)
else:
    print("this")
x=15
m=1
while x>=1:
    m=m*x*(x-1)
    x = x-2
    print(m)

def fact(x):
    if x==1:
        return 1
    else :
        return x*fact(x-1)
print(fact(15))

m=1
for i in range(5,0):
    print(i)



