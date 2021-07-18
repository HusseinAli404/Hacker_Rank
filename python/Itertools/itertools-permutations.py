# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import itertools

line = input().split()
word = line[0]
k = int(line[1])

permutations = list(itertools.permutations(word, k))
permutations.sort()

for permutation in permutations:
    print(''.join(permutation))
