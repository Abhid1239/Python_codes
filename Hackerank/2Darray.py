def hourglassSum(arr):
    i,j,m,n=[0,0,0,0]
    rows, cols = (4, 4) 
    sum = [[0 for i in range(cols)] for j in range(rows)]
    print(sum)
    while (i<8):
        if (i==4):
            m=2
            n=0
        #print('the number of time for 1st loop',i)
        while (j<4):
            #print('the number of time for 2nd loop',i,n,j,m,end='=')
            sum[n][j]=sum[n][j]+arr[i-m][j]+arr[i-m][j+1]+arr[i-m][j+2]
            
            print(arr[i-m][j]+arr[i-m][j+1]+arr[i-m][j+2])
            print(sum[n][j])
            print(sum)
            print()
            
            j=j+1
            
        n=n+1
        i=i+1
        j=0
    i,j=[1,1]
    print(i,j)
    while(i<5):
        print('the number of time for 1st loop',i)
        while (j<5):
            print('the number of time for 2nd loop',j)
            sum[i-1][j-1]=sum[i-1][j-1]+arr[i][j]
            j=j+1
        j=1
        i=i+1
    print(sum)
    num=max(map(max, sum))
    '''
    for val in range(0,3):
        for nv in range(3):
            print(sum[val][nv])'''
            
    return num        
        
        
        

            

arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

print(arr)



result = hourglassSum(arr)
print(result)

    
