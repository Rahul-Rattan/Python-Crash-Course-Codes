import random

def guess(number):
    random_number=random.randint(1,20)
    if number==random_number:
        print("Correct")
    else:
        print("Incorrect")


def main():
    number=int(input("Enter a number between 1 to 20: "))
    if 1<=number<=20:
        guess(number)
    else:
        print("Enter a valid number")

main()