# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import itertools

line = input().split()
word = sorted(line[0])
k = int(line[1])

for i in range(1, k + 1):
    for j in itertools.combinations(word, i):
        print(''.join(j))
