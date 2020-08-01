class shopping():
    def __init__(self,list_shop):
        self.list_s=list_shop

    def pri(self):
        print() 
        for li in self.list_s:
            print(li,end='  ')
    def add(self,obj):
        self.list_s.append(obj)
    def done(self,obj):
        self.list_s.remove(obj)



listt=['apple','mango','carrot','banana']
shop=shopping(listt)
shop.pri()
shop.add('rice')
shop.pri()
shop.done('carrot')
shop.pri()
