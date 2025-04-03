class Vehicle:
    def genaralUasage(self):
        print("Genaral usage: Transportation")

class Car(Vehicle):
    def __init__(self):
        self.wheel=4
        self.roof =True

    def specificUse(self):
        print("Specific Use: Work,Vaccation,Family")

class Bike(Vehicle):
    def __init__(self):
        self.wheel=2
        self.roof=False
    
    def specificUse(self):
        print("Specific Use: Road Trip,Racing")


c=Car()
c.genaralUasage()
c.specificUse()

m=Bike()
m.specificUse()

print(issubclass(Car,Bike))
print(isinstance(m,Vehicle))