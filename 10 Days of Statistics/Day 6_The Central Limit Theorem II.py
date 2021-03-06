# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import math

def cdf(std_dev, avg, x):
    inner = 1 + math.erf((x - avg) / (std_dev * math.sqrt(2)))
    return inner * 0.5

ans = cdf(math.sqrt(100) * 2.0, 100 * 2.4, 250)

print round(ans, 4)