def sockMerchant(n, ar):
    x=0
    a=0
    ar.sort()
    print(ar,len(ar))
    while x<(n-1):
        if ar[x]==ar[x+1]:
            #print(x)
            a=a+1
            x=x+2
            print(x,'value for if after plus 2')
            print(a,'number of times')
        else:
            x=x+1
            print(x,'value for else')
    return a


n = int(input())

ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)


print(str(result) + '\n')
