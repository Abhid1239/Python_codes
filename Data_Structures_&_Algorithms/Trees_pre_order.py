class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree :
    def __init__ (self, head):
        self.head = Node(head)

    def pre_search (self, val, start = 0):
        if start == 0:
            start = self.head
        if start:
            if start.value == val:
                return True
            else :
                return self.pre_search(val, start.left) or self.pre_search(val, start.right)
        return False

    def pre_all (self, traverse = "", start = 0):
        if start == 0:
            start = self.head
        if start:
            traverse += str(start.value) + " - "
            traverse = self.pre_all(start.left, traverse)
            traverse = self.pre_all(start.right, trasverse)
        return traverse

    
            

t = Tree(1)
t.head.left = Node(2)
t.head.right = Node(3)
t.head.left.left = Node(4)
t.head.left.right = Node(5)
t.head.right.left = Node(6)
t.head.right.left = Node(7)

print(t.pre_all())

print(t.pre_search(4))
print(t.pre_searc(14))

'''
+ - plus and minusses problem
for n in range(int(input())):
    char = input()

    res = 0

    for x in range(0,10000):
        cur = x
        ok = True

        for m in char:
            res = res + 1
            if m == '+':
                cur = cur + 1
            else:
                cur = cur - 1
            if cur < 0:
                ok = False
                break
        if ok:
            break

    print(res)

    '''

    
