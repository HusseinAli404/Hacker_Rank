# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import numpy

dimensions = tuple(map(int, input().split()))
print(numpy.zeros(dimensions, dtype=numpy.int))
print(numpy.ones(dimensions, dtype=numpy.int))
