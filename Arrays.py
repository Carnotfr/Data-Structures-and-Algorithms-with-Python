import numpy as np
from array import *

myArray1 = array('i', [1, 2, 3, 4, 5, 6, 7])
myArray2 = array('d', [1.5, 3, 4, 5.4, 2.4, 5.7])

print(myArray1)

# Insert a new element in the array
myArray1.insert(8, 8)
myArray1.insert(0, 0)

print(myArray1)

# Array traversal


def traverseArray(array):
    for i in array:
        print(i)


print(len(myArray1))

# Accessing an element in the array


def accessElement(array, index):
    if index >= len(array):
        print("Index out of range")
    else:
        print(array[index])


print(myArray1)

accessElement(myArray1, 10)

# Searching an element in the array


def searchElement(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in the array"


print(searchElement(myArray1, 5))

# Deletion of an element in the array
# myArray1.remove()

# Append a value in the array
myArray1.append(9)

# Two dimensional array

twoDimArray = np.array([[1, 2, 4, 5, 22, 5, 3, 45, 76], [
                       3, 4, 8, 26, 9, 54, 89, 76, 0, 98], [4, 1, 5, 4, 3, 2, 8, 8, 7]])

print(twoDimArray)
