
# Searching algorithms - Binary Search
import math
def binarySearch(array, value):
    start = 0
    end = len(array) - 1
    middle = math.floor((start+end)//2)
    while not(array[middle]==value) and start<=end:
        if value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1 
    if value == array[middle] :
        return middle
    else:
        return "Value not found"
        



custArray = [8, 9, 12, 15, 17, 19, 20, 21, 28]
print(binarySearch(custArray, 15))
# [8, 9, 12, 15, 17, 19, 20, 21, 28]
#  S              M               E
#  S  M      E
#        SM  E
#            SME