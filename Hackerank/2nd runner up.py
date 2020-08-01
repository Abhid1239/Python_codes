
def runnerup(le,arr):
    large,sl=-100,-100
    for n in arr:
        if large<n:
            large,sl=n,large
            print(large)
        elif (sl<n and large>n):
            sl=n
            print(sl,large)
            
        
for n in arr:
        if large<=n:
            large=n
            #print(large)
    #print(arr,sl,large)
    for x in arr:
        print(x,sl,large)
        if (sl<=x) and large!=x:
            print(sl)
            sl=x
    return sl
    return sl

    

n = int(input())
arr = map(int, input().split())
print(runnerup(n,arr))
