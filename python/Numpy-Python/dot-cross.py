# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import numpy
numpy.set_printoptions(legacy='1.13')


def zero(size):
    return [0 for _ in range(size)]


def get_matrix(size):
    matrix = []
    for _ in range(size):
        matrix.append(list(map(int, input().split())))
    return matrix


N = int(input())
matrix1 = numpy.array(get_matrix(N))
matrix2 = numpy.array(get_matrix(N)).transpose()

result = []
for row in range(N):
    result.append(zero(N))
    for column in range(N):
        result[row][column] = int(numpy.dot(matrix1[row], matrix2[column]))

print(numpy.array(result))
