'''def main():
 # Write code here 
    n= int(input())
    power=input().rstrip().split()
    chem=input().rstrip().split()
    v=0
    val=[]
    for p in range(n):
        val.append(int(chem[p])/int(power[p]))
    print(min(val))

main()

def main2():
    t=int(input())
    for n in range(t):
        g=list()'''


def runnerup(le,arr):
    large,sl=0,-100
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
            
        
    #print(arr,sl,large)
    '''
    for x in arr:
        print(x)
        print(n,sl,large)
        if (sl<=n) and sl<large:
            print(sl)
            sl=n
    print(arr,sl,large)'''
    return sl

    

n = int(input())
arr = list(map(int, input().split()))
print(runnerup(n,arr))
