# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
