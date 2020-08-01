#permutation of 1 number
def per(n):
    new=1
    for val in range(1,n+1):
        new=new*val
    return new

print(per(int(input())))

#permuation of 3 numbers and for n numbers


def gcd(a,b):
    if a>b:
        return gcd(a-b,b)
    elif a<b:
        return gcd(a,b-a)
    else:
        return a

print(gcd(16,23))
