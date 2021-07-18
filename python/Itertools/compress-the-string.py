# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import itertools

line = input()
result = ''

for entry in itertools.groupby(line):
    count = 0
    for element in entry[1]:
        count += 1
    result += str((count, int(entry[0]))) + ' '

print(result)
