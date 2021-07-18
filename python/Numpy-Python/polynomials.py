# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import numpy
numpy.set_printoptions(legacy='1.13')

polynomial = list(map(float, input().split()))
x = float(input())
value = numpy.polyval(polynomial, x)
print(value)
