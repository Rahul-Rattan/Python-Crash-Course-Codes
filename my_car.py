from car import Car,ElectricCar

my_new_car=Car("Audi", "A8", 2035)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading=23
my_new_car.read_odometer()

my_leaf=ElectricCar("Nissan","Leaf", 2024)
print(my_leaf.get_descriptive_name())