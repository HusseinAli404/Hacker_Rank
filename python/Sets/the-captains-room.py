# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
k = int(input())
array = list(map(int, input().split()))

frequencies = dict()

for element in array:
    frequencies[element] = (frequencies[element] if element in frequencies else 0) + 1

for key in frequencies:
    if frequencies[key] == 1:
        print(key)
        break
