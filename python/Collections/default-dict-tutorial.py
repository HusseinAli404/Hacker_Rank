# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

import collections


n, m = map(int, input().split())
frequencies = collections.defaultdict(list)

for i in range(n):
    word = input()
    frequencies[word].append(i + 1)

for _ in range(m):
    word = input()
    if len(frequencies[word]) > 0:
        print(' '.join(map(str, frequencies[word])))
    else:
        print(-1)
