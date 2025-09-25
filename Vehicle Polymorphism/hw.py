#START
class BMW:
    def fuel_type(self):
        print("BMW uses Petrol")

    def max_speed(self):
        print("BMW max speed: 250 km/h")

class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")

def car_details(car):
    car.fuel_type()
    car.max_speed()

bmw_car = BMW()
ferrari_car = Ferrari()
print("BMW Details:")
car_details(bmw_car)
print("\nFerrari Details:")
car_details(ferrari_car)
#END