# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

import math

AB = int(input())
BC = int(input())
h = math.sqrt(pow(AB, 2) + pow(BC, 2))
print(str(round(math.degrees(math.acos(BC / h)))) + '°')
