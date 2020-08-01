n = int(input())
def water(x):
    for x in range(1,n):
        if x % 2 == 0:
            if (n -x) % 2 == 0:
                return "YES"

    return "NO"

print(water(n))
