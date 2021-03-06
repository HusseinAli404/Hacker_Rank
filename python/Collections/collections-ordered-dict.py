# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

import collections


n = int(input())

prices = collections.OrderedDict()

for i in range(n):
    line = input().split()
    cost = int(line[len(line) - 1])
    name = ' '.join(line[0:len(line) - 1])
    if name in prices:
        prices[name] += cost
    else:
        prices[name] = cost


for key in prices:
    print(key, prices[key])
