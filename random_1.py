import random

a=[2,5,6,7,8,34,5,3,3,7,7,2]
b=[0,10,20,30]
print(b+a)
print(b*2)


e=2
d=e
e=e+2
print(e,d)

a=[1,2,3,4,5,6,7,8,9]
b=a[0:5]
a.append(4)
print(a,b)

i=0
while i<len(a):
    print(a[i])
    i+=1

def main():
    x = 1 # x represents an int value
    y = [1, 2, 3] # y represents a list 
    m(x, y) # Invoke f with arguments x and y
    print("x is " + str(x))
    print("y[0] is " + str(y[0]))

def m(number, numbers):
    number = 1001 # Assign a new value to number
    numbers[0] = 5555 # Assign a new value to numbers[0]


main()

matrix = [] # Create an empty list
numberOfRows = eval(input("Enter the number of rows: "))
numberOfColumns = eval(input("Enter the number of columns: "))
for row in range(0, numberOfRows):
    matrix.append([]) # Add an empty new row
    for column in range(0, numberOfColumns):
        value = eval(input("Enter an element and press Enter: "))
        matrix[row].append(value)
print(matrix)
