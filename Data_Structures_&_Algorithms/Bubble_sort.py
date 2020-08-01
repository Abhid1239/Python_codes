#arr = list(map(int,input().split()))
arr = [9, 4, 5, 24, 54, 6, 2, 5, 35]
def bubble(arr):
    l = 0
    for x in range(len(arr)):
        for n,m in zip(range(len(arr)-1-x),range(1,len(arr)-x)):
            print(str(n)+str(m), end = " ")
            l +=1
            if arr[n] > arr[m]:
                       arr[n], arr[m] = arr[m], arr[n]
        print(x)
    print("\n", l)
    return arr
                   

print(bubble(arr))

print(arr)

