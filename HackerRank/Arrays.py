import numpy

def arrays(arr):
    b=numpy.array(arr,float)
    c = numpy.array(list((reversed(b))))
    return c

arr = input().strip().split(' ')
result = arrays(arr)
print(result)