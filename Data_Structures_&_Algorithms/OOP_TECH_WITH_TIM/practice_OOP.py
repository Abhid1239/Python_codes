class car():
    list_milage = []
    count = 0
    def __init__ (self, company, milage):
        self.company = company
        self.milage = milage
        car.count = car.count + 1
        car.list_milage.append(milage)

    def max_avg (self):
        return max(car.list_milage)


class performance():
    car = []
    count = 0
    def __init__ (self,cars):
        self.cars = cars
        performance.count += 1
        performance.car.append(self.cars)
        
    def avg_mil_car (self):
        for comp in performance.car:
            print(self.cars.max_avg(),comp.milage)
            if self.cars.max_avg() == comp.milage:
                print(comp.company)
        
        

c1 = car("tata",50)
c2 = car("audi",60)
c3 = car("bmw", 70)

print(c1.max_avg())

p1 = performance(c1)
p2 = performance(c2)
p3 = performance(c3)

print(performance.count)
p1.avg_mil_car()




