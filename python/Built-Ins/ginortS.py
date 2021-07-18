# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
line = sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c))
print(''.join(line))
