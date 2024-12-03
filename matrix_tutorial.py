import random

matrix=[]

numberOfrows=eval(input("Enter Number of rows"))
numberOfcolumns=eval(input("Enter Number of Columns"))

for row in range(0, numberOfrows):
    matrix.append([])
    for column in range(0, numberOfcolumns):
        matrix[row].append(random.randrange(0,100))

print(matrix)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
for row in range(0, len(matrix)):
    for column in range(0, len(matrix[row])):
        print(matrix[row][column], end = " ")
print() # Print a newline

for row in range(0, len(matrix)):
    for column in range(0,len(matrix[row])):
        print(matrix[column][row], end=' ')
print()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Assume a list is given
total = 0
for column in range(0, len(matrix[0])):
    for row in range(0, len(matrix)):
        total += matrix[row][column]
    print("Sum for column " + str(column) + " is " + str(total))

for row in range(0, len(matrix)):
    for column in range(0, len(matrix[row])):
        i = random.randrange(0, len(matrix))
        j = random.randrange(0, len(matrix[row]))
        # Swap matrix[row][column] with matrix[i][j]
        matrix[row][column], matrix[i][j] = \
        matrix[i][j], matrix[row][column]
print(matrix)

scores = [
[[9.5, 20.5], [9.0, 22.5], [15, 33.5], [13, 21.5], [15, 2.5]],
[[4.5, 21.5], [9.0, 22.5], [15, 34.5], [12, 20.5], [14, 9.5]],
[[6.5, 30.5], [9.4, 10.5], [11, 33.5], [11, 23.5], [10, 2.5]],
[[6.5, 23.5], [9.4, 32.5], [13, 34.5], [11, 20.5], [16, 9.5]],
[[8.5, 26.5], [9.4, 52.5], [13, 36.5], [13, 24.5], [16, 2.5]],
[[9.5, 20.5], [9.4, 42.5], [13, 31.5], [12, 20.5], [16, 6.5]]]

for row in range(len(scores)):
    for column in range(len(scores[row])):
        for ed in range(len(scores[row][column])):
            print(scores[row][column][ed])
