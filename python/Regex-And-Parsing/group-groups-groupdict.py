# https://www.hackerrank.com
# https://github.com/hussein-ali-mc
import re

pattern = r'([a-zA-Z0-9])\1+'
match = re.search(pattern, input().strip())
print(match.groups()[0] if match else -1)
