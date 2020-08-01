
def tre(arr,n):
    i, x = 1, 0
    while i < n-1:
        if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
            print("YES")
            print(i,i+1,i+2)
            x = 1
            break
        i += 1
    if x == 0:
            print("NO")

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    tre(arr,n)
        
        
        
            
        
    
        
        
