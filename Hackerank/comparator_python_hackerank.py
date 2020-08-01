

def qui(arr, x, y, num):
    if  x < y:
        i = x - 1
        for j in range(x,y):
            num += 1
            if arr[j][1] > arr[y][1]:
                i += 1
                arr[i] , arr[j] = arr[j], arr[i]
            elif arr[j][1] == arr[y][1] :
                if arr[j][0] < arr[y][0]:
                    arr[y] , arr[j] = arr[j], arr[y]
                

        arr[i+1], arr[y] = arr[y], arr[i+1]
        p = i+1
        qui(arr, x, p-1,num)
        qui(arr, p+1, y,num)
    
        


def comparator(n):
        qui(n,0,len(n)-1, 0)
        print(n)


n = int(input())
data = []
for i in range(n):
    name, score = input().split()
    score = int(score)
    data.append([name,score])

comparator(data)

