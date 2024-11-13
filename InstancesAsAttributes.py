class Car:
    def __init__(self, make , model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    
    def get_descriptive_name(self):
        print(f"{self.year} {self.make} {self.model}")

    def read_odometer(self):
        print(f"This car has {self.odometer_reading}-miles on it")
    
    def update_odometer(self, mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("You cannot rollback odomter")
    
    def incement_odometer(self, miles):
        self.odometer_reading+=miles

my_new_car=Car('audi', 'A4', 2024)
my_new_car.get_descriptive_name()
my_new_car.read_odometer()

my_new_car.update_odometer(100)
my_new_car.read_odometer()

my_new_car.incement_odometer(25)
my_new_car.read_odometer()


class Battery:
        
        def __init__(self, battery_size=40):
             self.battery_size=battery_size
             
        def describe_battery(self):
            print(f"This car has a {self.battery_size}-kwh battery.")

        def fill_gas_tank(self):
            print("This car doesn't have a gas tank.")

        def get_range(self):
            if self.battery_size==40:
                range=150
            elif self.battery_size==65:
                range=225
            
            print(F"This car has {range} miiles on full charge.")



class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery=Battery()




my_leaf=ElectricCar('nissan', 'leaf', 2024)
my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()