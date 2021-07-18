# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
length = int(input())
tokens = input().split()
data = list(map(int, tokens))
t = tuple(data)
print(hash(t))
