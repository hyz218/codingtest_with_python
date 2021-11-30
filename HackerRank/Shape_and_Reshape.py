import numpy

arr = list(map(int,input().split(' ')))
my_arr = numpy.array(arr)
my_arr.shape = (3,3)

print(my_arr)