# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import collections

frequencies = collections.OrderedDict()
n = int(input())
for i in range(n):
    word = input()
    if word in frequencies:
        frequencies[word] += 1
    else:
        frequencies[word] = 1

print(len(frequencies))

for word in frequencies:
    print(frequencies[word], end=' ')
