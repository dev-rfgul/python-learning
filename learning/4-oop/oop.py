class Car:
    total_cars=0
    def __init__(self,userbrand,usermodel):
       self.brand=userbrand
       self.model=usermodel
       Car.total_cars+=1
    def full_name(self):
        print(f"the car is {self.brand} {self.model}")
    def fuel_type(self):
        return "petrol or diesel"

my_car=Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)


my_new_car=Car("Honda", "Accord")
print(my_new_car.brand)
print(my_new_car.model)

my_car.full_name()

new_new_car=Car.full_name(my_new_car)




#inheritence

class Electric_car(Car):
    def __init__(self,brand, model , battery_size):
        super().__init__(brand,model)
        self.battery_size=battery_size
        
    def fuel_type(self):
        return "Electric Charge"

my_tesla=Electric_car("Tesla","Model S", 100)
my_tesla.full_name()



#Encapsulation 

class Car2:
    def __init__(self, brand, model):
        self.model=model
        self.__brand=brand
    def get_brand(self):
        return self.__brand

    def full_name(self):
        print( f"the full name of the car is {self.__brand} {self.model}")
        
car2=Car2("car2 brand","car2 model")
car2.full_name()
# print(car2.brand) will give errors
print(car2.get_brand())



#Polymorphism

toyota=Car("totota", "Corolla")
tesla=Electric_car("Tesla","Model S","78")
print(toyota.fuel_type())
print(tesla.fuel_type())


print(Car.total_cars)