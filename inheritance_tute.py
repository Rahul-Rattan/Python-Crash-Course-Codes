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


class ElectricCar(Car):

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.batery_size=40

    def describr_battery(self):
        print(f"This car has a {self.batery_size}-kwh battery.")

    def fill_gas_tank(self):
        print("This car doesn't have a gas tank.")


my_leaf=ElectricCar('nissan', 'leaf', 2024)
my_leaf.get_descriptive_name()
my_leaf.describr_battery()