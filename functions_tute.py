def greet():
    print("Hello, World!")

greet()

unprinted_designs=['phone case','robot pendent', 'dodecahedronh']
completed_models=[]

def printing_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design=unprinted_designs.pop()
        print(f"We're currently printing: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("The following models have been completed")
    for completed_model in completed_models:
        print(completed_model)

printing_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


def build_profiles(first, last, **user_info):
    user_info["first_name"]=first
    user_info["last_name"]=last
    return user_info

user_profile=build_profiles('albert','einstein', location='princeton',field='Physics')

print(user_profile)