L=[1,3,5,7,8,4,3,6,9,2]
L.sort()
print(L)


def b_s(small,lar,L,find):
    mid = (lar + small)//2
    if small != mid :
        if find == L[mid]:
            return mid
        elif find < L[mid]:
            print(small, mid, find,n-1,'smallest')
            return b_s(small, mid, L, find)
        else :
            print('middle',mid,'largest', lar, find,'largest')
            return b_s(mid, lar, L, find)
            
    else:
        return -1


num=int(input())
m=b_s(0,len(L),L,num)
print(m,'The location number of the number',num)
