'''
num = 0
for n in range(int(input())):
    n, m, l = map(int,input().split())
    if n+m+l >=2 :
        num += 1
print(num)
scma
'''
def xyz(x,y):
    num = 0
    while x > y:
        if y*8 <= x:
            y = y*8
            num +=1
        elif y*4 <= x:
            num += 1
            y = y*4
        else:
            num +=1
            y = y*2

    if x != y:
        return -1
    else:
        return num
    
for num in range(int(input())):
    x , y = map(int,input().split())
    print(xyz(max(x,y),min(x,y)))
