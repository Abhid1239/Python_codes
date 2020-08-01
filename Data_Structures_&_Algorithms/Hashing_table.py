"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, strin):
        loc = self.calc_hash_val(strin)
        if self.table[loc] != None:
            self.table[loc].append(strin)
        else:
            self.table[loc] = strin
        

    def lookup(self, string):
        loc = self.calc_hash_val(string)
        if self.table[loc] != None:
            if string in self.table[loc]:
                return loc
        return -1

    def calc_hash_val (self, string):
        hash_v = ord(string[0])*100 + ord(string[1])
        return hash_v
'''
        
class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hv = self.calc_hash_val(string)
            if self.table[hv] != None:
                self.table[hv].append(string)
            else:
                self.table[hv] = [string]

    def lookup(self, string):
        hv = self.calc_hash_val(string)
        if self.table[hv] != None:
            if string in self.table[hv]:
                return hv
        return -1

    def calc_hash_val(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value'''
    
# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print(hash_table.calc_hash_val('UDACITY'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('UDACITY'))

# Test store
hash_table.store('UDACITY')
# Should be 8568
print(hash_table.lookup('UDACITY'))

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print(hash_table.lookup('UDACIOUS'))
