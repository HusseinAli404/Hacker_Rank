# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import numpy
numpy.set_printoptions(legacy='1.13')

A = numpy.array(list(map(int, input().split())))
B = numpy.array(list(map(int, input().split())))

print(numpy.inner(A, B))
print(numpy.outer(A, B))
