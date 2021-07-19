
# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import math

n = float(raw_input())
X = raw_input()

X = X.split(' ')
X = [int(x) for x in X]

mean = sum(X) / n

num = 0
for x in X:
    num = num + (x - mean)**2
    
std_dev = math.sqrt(num / n)
print std_dev