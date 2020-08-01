
class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def all_element(self):
        curr = self.head
        while curr.next:
            print(curr.value,curr.next.value ,end = "\t")
            curr = curr.next
        print(curr.value,curr.next)

        
    def insert_first(self, new_e):
        new_e.next = self.head
        self.head = new_e
        "Insert new element as the head of the LinkedList"
    

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        curr = self.head
        self.head = self.head.next
        return curr
        

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        self.ll.insert_first(new_element)
        "Push (add) a new element onto the top of the stack"
        

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        
    def all(self):
        self.ll.all_element()
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
stack.all()
print(stack.pop().value)
