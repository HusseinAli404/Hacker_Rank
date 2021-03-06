# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

import re


line = input()
substring = input()
pattern = re.compile(substring)

match = pattern.search(line)
if match is None:
    print((-1, -1))

while match:
    print('({}, {})'.format(match.start(), match.end()))
    match = pattern.search(line, match.start() + 1)
