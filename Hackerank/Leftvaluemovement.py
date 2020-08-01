def rotLeft(a,v,d):
    sum=[]
    for val in range(d,v):
        sum.append(a[val])
    for val in range(d):
        sum.append(a[val])
    return sum











d = int(input())

a = list(map(int, input().rstrip().split()))

v = len(a)
result = rotLeft(a,v, d)
print(result)
