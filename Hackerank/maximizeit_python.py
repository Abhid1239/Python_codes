K, M = map(int,input().split())
arrayN = []
for _i_ in range(K):
    arrayN.append([int(x) for x in input().split()][1:])
    
from itertools import product
possible_combination = list(product(*arrayN))
print(possible_combination)
