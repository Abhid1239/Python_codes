class node():
    def __init__(self,element):
        self.element = element
        self.next = None
class Stack():
    def __init__(self,head):
        self.head = head

    def push (self, node):
        if self.head:
            node.next = self.head
            self.head = node
        else:
            self.head = node

    def p_all(self):
        curr = self.head
        if self.head:
            while curr.next :
                print(curr.element, curr.next.element, end = "\t")
                curr = curr.next
            print(curr.element, curr.next)
        else:
            print(curr)

    def pop(self):
        curr = self.head
            #print(curr.element)
        if curr.next == None:
            self.head  = None
        else:
            self.head = curr.next


n1 = node(5)
n2 = node(6)
n3 = node(7)
n4 = node(8)
n5 = node(12)
n6 = node(4)

s1 = Stack(10))
s1.push(6)
s1.p_all()

