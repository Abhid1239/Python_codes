class element:
    def __init__(self,value):
        self.value = value
        self.next = None


class Linkylist:
    def __init__(self,head):
        self.head = head

    def add_element(self,num):
        curr = self.head
        while curr.next :
            curr = curr.next
        curr.next = num
        num.next = None
        
    def all_element(self):
        curr = self.head
        while curr.next:
            print(curr.value,curr.next.value ,end = "\t")
            curr = curr.next
        print(curr.value,curr.next ,end = "\t")
        print("\n")
        
    def remove_loc(self,loc):
        curr, prev, count = self.head, None, 1
        if loc > 1:
            print(curr.value, curr.next.value,count)
            while curr and count < loc -1 :
                curr = curr.next
                count += 1
            if curr.next.next == None:
                curr.next = prev
            else:
                curr.next = curr.next.next
    
        else :
            self.head = curr.next

    def delete_val(self, value):
        current = self.head
        previous = None
        while current.value != value and current.next:
            previous = current
            current = current.next
        if current.value == value:
            if previous:
                previous.next = current.next
            else:
                self.head = current.next

    def insert_loc(self, val, loc):
        curr, prev, count = self.head, None, 1 
        while count != loc and curr:
            prev, curr = curr, curr.next
        if prev :
            prev.next, val.next = val ,curr.next
        else :
            self.head,val.next = val, curr
            
        


e1 = element(10)
e2 = element(5)
e3 = element(2)
e4 = element(9)
e5 = element(6)
e6 = element(4)

l = Linkylist(e1)
l.add_element(e2)
l.add_element(e3)
l.add_element(e4)
l.add_element(e5)
l.add_element(e6)


l.all_element()  
l.remove_loc(1)  
l.all_element()         # 5 2

l.delete_val(4)
l.all_element()         # 5

l.add_element(e1)
l.all_element() 


l.remove_loc(4)  
l.all_element()         # 5 2

l.delete_val(2)
l.all_element()         # 5


l.insert_loc(e3,1)
l.all_element()         # 10 5 2




    
