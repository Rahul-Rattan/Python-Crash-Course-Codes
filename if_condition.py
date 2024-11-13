cars=["subaru", 'bmw','audi','volkswagon', 'jeep', 'mercedez', 'toyota', 'honda']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(f"{car.title()}")

user = 'Tata'
if user not in  cars:
    print(f'you may add {user} to the list')
cars.insert(0,user)
print(cars)