class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)


    def insert(self, new_val):
        self.i(new_val, self.root)
        
        
    def i(self, new_val, curr):
        if curr.value > new_val:
            if curr.left :
                self.i(new_val,curr.left)
            else:
                curr.left = Node(new_val)
        else:
            if curr.right :
                self.i(new_val,curr.right)
            else:
                curr.right = Node(new_val)
        
        
    def search(self,find_val):
        return self.se(find_val, self.root)

    def se(self, find_val, curr):
        while curr :
            if curr.value == find_val:
                return True
            else :
                if curr.value < find_val:
                    return self.se(find_val,curr.right)
                else:
                    return self.se(find_val, curr.left)
        return False
        
        
    def pri(self):
        return self.p_all(self.root,[])
        
    
    def p_all(self,start,lis):
        if start :
            lis.append(start.value)
            lis = [self.p_all(start.left,lis)]
            lis = [self.p_all(start.right,lis)]
        return lis
            
            
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)
print(tree.pri())
# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
