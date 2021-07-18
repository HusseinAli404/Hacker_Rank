# https://www.hackerrank.com
# https://github.com/hussein-ali-mc

n = int(input())
tokens = map(int , input().split())
plants = set(tokens)
print(sum(plants) / len(plants))
