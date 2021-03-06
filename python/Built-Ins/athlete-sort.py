# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
N, M = map(int, input().split())
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

K = int(input())
data = sorted(data, key=lambda x: x[K])

for row in data:
    print(' '.join(map(str, row)))
