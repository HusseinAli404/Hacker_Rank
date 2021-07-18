# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
m = int(input())
M = set(map(int, input().split()))

n = int(input())
N = set(map(int, input().split()))

D = M.symmetric_difference(N)
array = list(D)
array.sort()

for element in array:
    print(element)
