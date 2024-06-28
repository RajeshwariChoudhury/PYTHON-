import numpy
def arrays(arr):
    arr1 = numpy.array(arr, dtype = int)
    arr2 = arr1.reshape(3, 3)
    return arr2

arr = input().strip().split(' ')
result = arrays(arr)
print(result)