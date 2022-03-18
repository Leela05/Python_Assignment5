# Write a Python program to square and cube every number
# in a given list of integers using Lambda

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(" list of integers:")
print(number)
print("\nSquare:")
square = list(map(lambda x: x ** 2, number))
print(square)
print("\nCube:")
cube = list(map(lambda x: x ** 3, number))
print(cube)