a=int(input())
b=int(input())
x,y=a,b

while a!=b and a>0 and b> 0:
        if a>b:
                a=a-b
        elif a<b:
                b=b-a
        elif a == b:
                print()
print(a,'this is hcf')

def gcd(x,y):
        print(x,y)
        if x == 0:
                return y
        return gcd(x % y, x)

print(gcd(x,y),'Another way of GCD')





# for lcm u can use 2 types 1 st a*b = LCM(a,b) * HCF (a,b)
#                       i.e LCM(a*b) = a*b / HCF (a,b)

# now find lcm directly we need to get the maximum number then see if their is remainder
# of the number by the smallest number if not equal then add the same number to it
# till we do not get the lcm
# hcf is opposiste see if the 

# lcm

print(x*y/a,'LCM value')

def LCM (a,b,high = 0):
        print(a,b,high)
        if high == 0:
                high = max(a,b)
        if high%a == 0  and high%b == 0:
                return high
        high = high+max(a,b)
        return LCM(a,b,high)

print(LCM(x,y),'LCM with function')
