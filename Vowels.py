
vowels='aeiouAEIOU'

for i in range(1,11):
    letter=input("Enter a letter: ")
    if letter.isalpha()==False:
        print(letter,"is an invalid input")
    elif letter in vowels:
        print(letter," is a vowel.")
    else:
        print(letter," is a consonant.")

a=[range(20)]
print(a)