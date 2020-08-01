arr = [9, 4, 5, 24, 54, 6, 2, 5, 35]

def merge(arr):
    if len(arr) > 1:
        m = len(arr)//2
        l = arr[:m]
        r = arr[m:]
        #print(l,r)

        merge(l)
        merge(r)
        #print()
        x, y, z = 0, 0, 0
        print(l, r)
        while x < len(l) and y < len(r):
            if l[x] > r[y]:
                arr[z] = r[y]
                y += 1
            else:
                arr[z] = l[x]
                x += 1
            z += 1

        while x < len(l):
            arr[z] = l[x]
            x, z = x + 1, z + 1

        while y < len(r):
            arr[z] = r[y]
            y, z = y + 1, z + 1



merge(arr)
print(arr)
    
