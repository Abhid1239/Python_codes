#arr = list(map(int,input().split()))
arr = [9, 4, 5, 24, 54, 6, 2, 5, 35]
def bubble(arr):
    n, m = 0, 0
    while n < len(arr) :
        m = m + n + 1
        while m < len(arr) :
            #print(n, m)
            if arr[n] > arr[m] :
                arr[n], arr[m] = arr[m], arr[n]
            m += 1
        m = 0
        n += 1
    return arr

print(bubble(arr))


def sort(arr):
        for ind,n in enumerate(arr):
                for i,m in enumerate(arr[ind+1:]):
                        print(arr)
                        if n > m :
                                n , m = m, n
                                arr[ind] , arr[i+ind+1] = arr[i+ind+1] , arr[ind]
                print(arr)
                print("")
        return arr


arr = [9, 4, 5, 24, 54, 6, 2, 5, 35]

print(sort(arr))
