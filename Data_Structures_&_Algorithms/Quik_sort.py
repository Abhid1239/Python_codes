
def qui(arr, x, y, num):
    if  x < y:
        i = x - 1
        for j in range(x,y):
            num += 1
            if arr[j] <= arr[y]:
                i += 1
                arr[i] , arr[j] = arr[j], arr[i]

        arr[i+1], arr[y] = arr[y], arr[i+1]
        p = i+1
        qui(arr, x, p-1,num)
        qui(arr, p+1, y,num)

'''
def sort (arr, x, p):
    if x < p:
        pi = '''
arr = [5,98,3,16,14, 3, 45,0, 8,34, 6]
n = len(arr)

qui(arr,0, n-1,0)
print(arr)
arr = [1,2,3,4,5,6,7,8]
n = len(arr)

qui(arr, 0, n-1,0)
print(arr)
arr = [8,7,6,5,4,3,2,1]
n = len(arr)

qui(arr, 0, n-1,0)
print(arr)
arr = [7, 3 , 9, 4, 5, 2, 0, 6]
n = len(arr)

qui(arr, 0, n-1,0)
print(arr)

def quik(arr, x, y,num):
    if x < y:
        i , j  = x , y
        while i < j:
            num += 1
            if arr[i] > arr[j]:
                arr[i], arr[j], arr[j-1] = arr[j-1], arr[i],arr[j]
                j -= 1
            else:
                i += 1
        print(num)
        quik(arr, x, j-1,num)
        quik(arr,j+1, y,num)

arr = [5,98,3,16,14, 3, 45,0, 8,34, 6]
n = len(arr)

quik(arr,0, n-1,0)
print(arr)
arr = [1,2,3,4,5,6,7,8]
n = len(arr)

quik(arr, 0, n-1,0)
print(arr)
arr = [8,7,6,5,4,3,2,1]
n = len(arr)

quik(arr, 0, n-1,0)
print(arr)
arr = [7, 3 , 9, 4, 5, 2, 0, 6]
n = len(arr)
quik(arr, 0, n-1,0)
print(arr)
