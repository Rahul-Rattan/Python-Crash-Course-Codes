alien2={'color':'green','points':5}
print(alien2['color'])
alien2['x_position']=0
alien2['y_position']=25
print(alien2)

alien={"x_position":0, 'y_position':25, 'color':'green', "speed":'medium'}
#Original x_position value
print(f"The original x_position is {alien['x_position']}" )

if alien["speed"]=='slow':
    x_increment=1

if alien["speed"]=='medium':
    x_increment=2

else:
    #This is a fast alien
    x_increment=3

alien["x_position"]=alien['x_position']+x_increment
print(f"New list with increment is {alien}")

user={
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
}
for k,v in user.items():
    print(f"\nKey:{k}")
    print(f"Value:{v}")

favourite_language={
    'phil': 'python',
    "eli":'rust',
    'edward':'C',
    'sarah':'python'
}

friends=['phil', 'sarah']
for name in favourite_language.keys():
    print(f"\nHi, {name.title()}!")

    if name in friends:
        print(f"{name.title()}, i see that you like {favourite_language[name]} language")
if 'erin' not in favourite_language.keys():
    print(f"Erin please take a poll.")

pizza={
    "crust":'thick',
    'toppings': ['mushrooms','extra cheese']
}
print(f"You ordered a {pizza['crust']} - crust pizza"
      ' with the following toppings :')

for topping in pizza['toppings']:
    print(f"\t{topping}")