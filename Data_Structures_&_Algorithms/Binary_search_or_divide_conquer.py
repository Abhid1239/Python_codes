'''def b( arr, v, s, l):
    if s <= l:
        m = (l+s)//2
        
        if arr[m] > v :
            return b( arr, v, s, m - 1)
        elif arr[m] < v:
            return b( arr, v, m + 1, l)
        else:
            return m
    else:
        return -1'''
        
def binary_search(arr, val):
    small = 0
    larg = len(arr) - 1
    while small <= larg:
        midd = (small + larg)// 2
        
        if arr[midd] < val :
            small = midd + 1
        elif arr[midd] > val:
            larg = midd - 1
        else :
            return midd
    return -1

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
