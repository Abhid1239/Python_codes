#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
    sums=[0]*16
    n=3
    #magic=[0 for i in range(n) for j in range(n)]
    magic = [[0 for i in range(3)] for j in range(3)] 
    num=[num for num in range(1,10)]
    z=0
    
    for x in range(0,n):
        for y in range(0,n):
            sums[z]+=s[x][y]
        z+=1
        if sums[z]==15:
            for x in range(0,n):
                for y in range(0,n):
                    magic[x][y]=s[x][y]
                    num.remove(s[x][y])
    print(sums)

    for x in range(0,n):
        for y in range(0,n):
            sums[z]+=s[y][x]
        z+=1
        if sums[z]==15:
            for x in range(0,n):
                for y in range(0,n):
                    magic[y][x]=s[y][x]
                    num.remove(s[y][x]) 
    '''else:
        for x in range(0,n):
            for y in range(0,n):
                extra[x]=s[y][x]'''


    
    for val in range(0,n):
        sums[z]+=s[val][val]
        if sums[z]==15:
            for val in range(0,n):
                magic[val][val]=s[val][val]
                num.remove(s[val][val])
    z+=1

    for val in range(0,n):
        sums[z]+=s[val][n-val-1]
        if sums[z]==15:
            for val in range(0,n):
                magic[val][n-val-1]=s[val][n-val-1]
                num.remove(s[val][n-val-1])
    z+=1
    z=0
    total=0
    print(magic)
    for val in magic:
        for v in val:
            total+=v

        if total!=15:
            if val.count(0)>=2:
                break
            else:
                insert_value=15-total
                insert_index=val.index(val.index(0),insert_val)
                val.insert(insert_index,insert_value)
                num.remove(insert_value)
        z+=1
    
    final=0
    for val in magic:
        final+=sum([v for v in val])

    if final==45:
        print(magic)

    else:
        print(magic)

    
    '''for x in range(n):
        total=sum[z]    
        if total!=15:
            
            if 
                break
            else:
                insert_value=15-total
                insert_index=val.index(n if n==0 for n in val)
                val.insert(insert_index,insert_value)
                num.remove(insert_vslue)'''
    

    
        





    
    
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
