#lenA, lenB = map(int, raw_input().split())
setA = map(int, raw_input().split())
setB = map(int, raw_input().split())

maxA = max(setA)
minB = min(setB)
count = 0
for num in range(maxA, minB + 1):
    left = all([num % numA == 0 for numA in setA])
    right = all([numB % num == 0 for numB in setB])
    count += left*right
print count

