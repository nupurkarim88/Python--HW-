#START 
class Vehicle:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare

class Bus(Vehicle):
    def total_fare(self, passengers):
        return self.fare * passengers

bus1 = Bus("City Bus", 10)
print("Total Fare:", bus1.total_fare(5))
#END