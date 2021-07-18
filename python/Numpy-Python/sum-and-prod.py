# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import numpy

N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

data = numpy.array(data)
data = data.sum(axis=0)
product = data.prod()
print(product)
