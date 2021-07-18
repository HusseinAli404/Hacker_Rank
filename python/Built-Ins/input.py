# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
x, k = map(int, input().split())
polynomial = input()
result = eval(polynomial)
print(result == k)
