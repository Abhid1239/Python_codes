a = {0:1, 1:9}
_sum = 0
for b in a:
    _sum +=b
    print(_sum)

print(_sum +b)


a=lambda x:x!=1
b=[n for n in range(5)]
print(b)
print(list(filter(a,b)))
print(len(list(filter(a,b))))

a = [3,2,1]
b=sorted(a)
print(b)
a.insert(0,1)
print(a)
print(b)
print(b[1])
