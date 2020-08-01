def getTotalX(a, b):
    minr,maxr=max(a),min(b)
    values=[]
    out=0
    
    y=0
    
    for a_num in a :
        for val in range(minr,maxr+1):
            if val%a_num==0 :
                values.append(val)
                print(val)
    x=[0]*(len(values)+len(b))
    values=set(values)
    for val in values:
        for b_num in b:
            if  b_num%val==0:
                x[y]=x[y]+1
                print(val)
        y=y+1
    print(x)
    for val in x:
        if val-(len(b))==0:
            print(val)
            out=out+1
    '''for a_num in a :
        for b_num in b:
            for val in range(minr,maxr+1):
                if a_val%num==0 and num%b_val==0 :
                    values[x][y]+=1
                y=y+1
        x=x+1'''
    return out
    
            
    # Write your code here



arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)
print(total)
