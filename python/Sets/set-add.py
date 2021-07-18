# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
n = int(input())
stamps = set()
for i in range(n):
    country = input()
    stamps.add(country)

print(len(stamps))
