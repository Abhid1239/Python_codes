class Person():
    def __init__ (self, name, age, ID):
        self.name = name
        self.age = age
        self.ID = ID

    def info(self):
        print("I am {} of age {} and my ID is {}".format(self.name,self.age,self.ID))

    def acc_pvt_files(self):
        print("ACCESS DENIED to primary user")

class manager(Person):
    def __init__(self,name,age,ID,level):
        super().__init__(name,age,ID)
        self.level = level
        
    def acc_pvt_files(self):
        print("ACCESS GRANTED to primary user")
        

class worker(Person):
    def __init__(self,name,age,ID,level):
        super().__init__(name,age,ID)
        self.level = leve
