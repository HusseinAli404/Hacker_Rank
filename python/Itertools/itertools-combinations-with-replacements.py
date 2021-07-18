# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import itertools

line = input().split()
word = sorted(line[0])
k = int(line[1])

for entry in itertools.combinations_with_replacement(word, k):
    print(''.join(entry))
